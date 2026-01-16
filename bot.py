import asyncio
import sqlite3
import os
import json
import random
import datetime
import hashlib
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gtts import gTTS
from openai import OpenAI
import logging
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ====== DATABASE ======
def init_db():
    db = sqlite3.connect("bot.db", check_same_thread=False)
    cur = db.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        language TEXT DEFAULT 'en',
        learned INTEGER DEFAULT 0,
        level TEXT DEFAULT 'Beginner',
        start_date TEXT,
        last_remind TEXT,
        last_active DATE DEFAULT CURRENT_DATE,
        lessons_count INTEGER DEFAULT 0,
        current_lesson_words JSON DEFAULT '[]', 
        current_word_index INTEGER DEFAULT 0
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS word_library(
        word TEXT,
        lang TEXT,
        reading TEXT,
        meaning TEXT,
        grammar TEXT,
        example TEXT,
        rank INTEGER,
        PRIMARY KEY (word, lang)
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS progress(
        user_id INTEGER,
        word TEXT,
        lang TEXT,
        date TEXT,
        strength INTEGER DEFAULT 0,
        PRIMARY KEY (user_id, word, lang)
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS daily_logs(
        user_id INTEGER,
        date TEXT,
        content JSON,
        PRIMARY KEY (user_id, date)
    )""")
    
    # NEW: Pending Tests Table
    cur.execute("""CREATE TABLE IF NOT EXISTS pending_tests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        run_at TEXT,
        words_json JSON
    )""")
    
    db.commit()
    return db

db = init_db()

def get_cursor():
    return db.cursor()

def tts(text: str, lang: str) -> str:
    try:
        if not text: return None
        text_hash = hashlib.md5(f"{text}_{lang}".encode()).hexdigest()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(base_dir, f"audio_{text_hash}.mp3")
        if os.path.exists(filename): return filename
        
        gtts_lang = lang if lang in ['en', 'ru', 'ar', 'tr'] else 'en'
        tts_obj = gTTS(text=text, lang=gtts_lang, slow=False)
        tts_obj.save(filename)
        return filename
    except: return None

# ====== LOGIC ======

async def get_next_curriculum_words(user_id: int, lang: str, count: int = 5):
    cur = get_cursor()
    query = """
    SELECT * FROM word_library 
    WHERE lang = ? 
    AND word NOT IN (SELECT word FROM progress WHERE user_id = ? AND lang = ?)
    ORDER BY rank ASC
    LIMIT ?
    """
    cur.execute(query, (lang, user_id, lang, count))
    return [{"word": r[0], "reading": r[2], "meaning": r[3], "grammar": r[4], "example": r[5]} for r in cur.fetchall()]

# ====== INTERACTIVE FLOW ======

async def start_interactive_lesson(user_id, lang, words):
    cur = get_cursor()
    cur.execute("UPDATE users SET current_lesson_words = ?, current_word_index = 0 WHERE user_id=?", 
                (json.dumps(words), user_id))
    db.commit()
    await show_current_word(user_id, lang)

async def show_current_word(user_id, lang):
    cur = get_cursor()
    cur.execute("SELECT current_lesson_words, current_word_index, learned FROM users WHERE user_id=?", (user_id,))
    res = cur.fetchone()
    if not res: return
    
    words_json, idx, learned_count = res
    words = json.loads(words_json)
    
    # END OF LESSON
    if idx >= len(words):
        # Schedule test in 3 hours
        # For DEMO/TESTING: Set to 10 seconds? No, user wanted 3 hours. 
        # But for user to see it works, I might log it.
        run_at = (datetime.datetime.now() + datetime.timedelta(hours=3)).isoformat()
        cur.execute("INSERT INTO pending_tests (user_id, run_at, words_json) VALUES (?, ?, ?)",
                    (user_id, run_at, words_json))
        db.commit()
        
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➡️ Keyingi Darsni Boshlash", callback_data="start_next")]
        ])
        
        msg = (f"🎉 <b>Dars tugadi!</b> {len(words)} ta so'z o'rganildi.\n"
               f"⏰ 3 soatdan keyin bilimingizni sinash uchun test yuboraman!\n\n"
               f"Hozir davom etamizmi?")
        await bot.send_message(user_id, msg, reply_markup=kb, parse_mode=ParseMode.HTML)
        return

    word_data = words[idx]
    text = f"📊 <b>Statistika:</b> {learned_count} so'z\n\n"
    text += f"✨ <b>{word_data['word']}</b>"
    if word_data.get('reading'): text += f"\n🗣 {word_data['reading']}"
    text += f"\n\n🇺🇿 <b>{word_data['meaning']}</b>"
    if word_data.get('grammar'): text += f"\n📚 {word_data.get('grammar')}"
    if word_data.get('example'): text += f"\n✍️ <i>{word_data.get('example')}</i>"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ Keyingisi", callback_data="next_word")]
    ])
    
    await bot.send_message(user_id, text, reply_markup=kb, parse_mode=ParseMode.HTML)
    
    fpath = tts(word_data['word'], lang)
    if fpath:
        try: await bot.send_voice(user_id, FSInputFile(fpath))
        except: pass
        
    today = datetime.date.today().isoformat()
    cur.execute("INSERT OR REPLACE INTO progress (user_id, word, lang, date, strength) VALUES (?, ?, ?, ?, 1)",
                (user_id, word_data['word'], lang, today))
    cur.execute("UPDATE users SET learned = learned + 1 WHERE user_id=?", (user_id,))
    db.commit()

@dp.callback_query(F.data == "next_word")
async def cb_next_word(call: CallbackQuery):
    cur = get_cursor()
    cur.execute("UPDATE users SET current_word_index = current_word_index + 1 WHERE user_id=?", (call.from_user.id,))
    db.commit()
    cur.execute("SELECT language FROM users WHERE user_id=?", (call.from_user.id,))
    lang = cur.fetchone()[0]
    await call.message.edit_reply_markup(reply_markup=None) 
    await show_current_word(call.from_user.id, lang)
    await call.answer()

@dp.callback_query(F.data == "start_next")
async def cb_start_next(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await process_daily_words_for_user(call.from_user.id)
    await call.answer()

# ====== DELAYED TEST SYSTEM ======

async def check_pending_tests():
    cur = get_cursor()
    now_str = datetime.datetime.now().isoformat()
    
    # Get due tests
    cur.execute("SELECT id, user_id, words_json FROM pending_tests WHERE run_at <= ?", (now_str,))
    rows = cur.fetchall()
    
    for row in rows:
        tid, uid, wjson = row
        try:
            words = json.loads(wjson)
            if not words: continue
            
            # Create a question
            target = random.choice(words)
            options = [w['meaning'] for w in words]
            random.shuffle(options)
            
            kb = []
            for opt in options:
                is_correct = "1" if opt == target['meaning'] else "0"
                kb.append([InlineKeyboardButton(text=opt, callback_data=f"test:{is_correct}")])
            
            text = f"⏰ <b>Tekshiruv Vaqti!</b>\n\nSo'zning tarjimasini toping:\n👉 <b>{target['word']}</b>"
            await bot.send_message(uid, text, reply_markup=InlineKeyboardMarkup(inline_keyboard=kb), parse_mode=ParseMode.HTML)
            
        except Exception as e:
            logger.error(f"Test error: {e}")
        
        # Delete completed test
        cur.execute("DELETE FROM pending_tests WHERE id=?", (tid,))
        db.commit()

@dp.callback_query(F.data.startswith("test:"))
async def answer_test(call: CallbackQuery):
    res = call.data.split(":")[1]
    msg = "✅ Barakalla! To'g'ri topdingiz." if res == "1" else "❌ Afsus, noto'g'ri."
    await call.message.edit_text(msg)

# ====== ADMIN & COMMANDS ======

@dp.message(Command("start"))
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇸🇦 Arab", callback_data="lang:ar"),
         InlineKeyboardButton(text="🇷🇺 Rus", callback_data="lang:ru")],
        [InlineKeyboardButton(text="🔄 Reset", callback_data="reset")]
    ])
    await message.answer("Assalomu alaykum! Tilni tanlang:", reply_markup=kb)

@dp.callback_query(F.data.startswith("lang:"))
async def cb_lang(call: CallbackQuery):
    lang = call.data.split(":")[1]
    cur = get_cursor()
    cur.execute("INSERT OR REPLACE INTO users (user_id, language, start_date, last_active, lessons_count) VALUES (?, ?, ?, ?, 0)",
                (call.from_user.id, lang, datetime.date.today().isoformat(), datetime.date.today().isoformat()))
    db.commit()
    await call.message.edit_text(f"✅ Til: {lang}")
    await process_daily_words_for_user(call.from_user.id)

@dp.message(Command("admin"))
async def cmd_admin(message: Message):
    txt = "🛠 <b>Admin</b>\n`/add lang|word|read|mean|gram|ex`\n`/broadcast Msg`"
    await message.answer(txt, parse_mode=ParseMode.HTML)

@dp.message(Command("add"))
async def cmd_add(message: Message):
    try:
        parts = message.text.replace("/add", "").strip().split("|")
        if len(parts) < 4: return await message.reply("Format error.")
        l, w, r, m = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
        g = parts[4].strip() if len(parts)>4 else ""
        e = parts[5].strip() if len(parts)>5 else ""
        
        cur=get_cursor()
        cur.execute("SELECT MAX(rank) FROM word_library WHERE lang=?", (l,))
        rank = (cur.fetchone()[0] or 0) + 1
        cur.execute("INSERT INTO word_library (word, lang, reading, meaning, grammar, example, rank) VALUES (?,?,?,?,?,?,?)",
                    (w,l,r,m,g,e,rank))
        db.commit()
        await message.reply(f"✅ Saved: {w}")
    except Exception as x: await message.reply(f"Err: {x}")

@dp.message(Command("broadcast"))
async def cmd_bd(message: Message):
    txt = message.text.replace("/broadcast", "").strip()
    if not txt: return
    cur = get_cursor()
    cur.execute("SELECT user_id FROM users")
    c=0
    for (u,) in cur.fetchall():
        try:
            await bot.send_message(u, f"📢 {txt}")
            c+=1
        except: pass
    await message.reply(f"Sent to {c}")

@dp.callback_query(F.data == "reset")
async def rst(c):
    cur=get_cursor()
    cur.execute("DELETE FROM progress WHERE user_id=?", (c.from_user.id,))
    cur.execute("UPDATE users SET learned=0, lessons_count=0, current_word_index=0 WHERE user_id=?", (c.from_user.id,))
    db.commit()
    await c.message.edit_text("Reset done.")

async def process_daily_words_for_user(user_id):
    cur = get_cursor()
    cur.execute("SELECT language FROM users WHERE user_id=?", (user_id,))
    res = cur.fetchone()
    if not res: await bot.send_message(user_id, "/start"); return
    
    words = await get_next_curriculum_words(user_id, res[0], 5)
    if not words: await bot.send_message(user_id, "Kurs tugadi!"); return
    await start_interactive_lesson(user_id, res[0], words)

async def main():
    scheduler = AsyncIOScheduler()
    # Check for tests every minute
    scheduler.add_job(check_pending_tests, 'interval', minutes=1)
    scheduler.start()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: asyncio.run(main())
    except: pass
