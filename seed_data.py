import sqlite3

def seed():
    db = sqlite3.connect("bot.db")
    cur = db.cursor()
    
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
    
    # --- RUSSIAN DATA (Restored) ---
    RU_DATA = [
        {"r": 1, "w": "Здравствуйте", "rd": "Zdravstvuyte", "m": "Assalomu alaykum", "g": "Greeting", "e": "Здравствуйте!"},
        {"r": 2, "w": "Привет", "rd": "Privet", "m": "Salom", "g": "Greeting", "e": "Привет!"},
        {"r": 3, "w": "Как дела?", "rd": "Kak dela?", "m": "Ishlar qalay?", "g": "Question", "e": "Как дела?"},
        {"r": 4, "w": "Спасибо", "rd": "Spasibo", "m": "Rahmat", "g": "Polite", "e": "Спасибо!"},
        {"r": 5, "w": "Пожалуйста", "rd": "Pozhaluysta", "m": "Iltimos", "g": "Polite", "e": "Пожалуйста."},
        {"r": 6, "w": "Да", "rd": "Da", "m": "Ha", "g": "Particle", "e": "Да."},
        {"r": 7, "w": "Нет", "rd": "Net", "m": "Yo'q", "g": "Particle", "e": "Нет."},
        {"r": 8, "w": "Я", "rd": "Ya", "m": "Men", "g": "Pronoun", "e": "Я здесь."},
        {"r": 9, "w": "Ты", "rd": "Ty", "m": "Sen", "g": "Pronoun", "e": "Ты кто?"},
        {"r": 10, "w": "Хорошо", "rd": "Khorosho", "m": "Yaxshi", "g": "Adverb", "e": "Хорошо."},
        {"r": 11, "w": "Семья", "rd": "Sem'ya", "m": "Oila", "g": "Noun", "e": "Моя семья."},
        {"r": 12, "w": "Папа", "rd": "Papa", "m": "Dada", "g": "Noun", "e": "Мой папа."},
        {"r": 13, "w": "Мама", "rd": "Mama", "m": "Oyi", "g": "Noun", "e": "Моя мама."},
        {"r": 14, "w": "Брат", "rd": "Brat", "m": "Aka/Uka", "g": "Noun", "e": "Где брат?"},
        {"r": 15, "w": "Сестра", "rd": "Sestra", "m": "Opa/Singil", "g": "Noun", "e": "Где сестра?"},
        {"r": 58, "w": "Большой", "rd": "Bol'shoy", "m": "Katta", "g": "Adjective", "e": "Большой дом."},
        {"r": 59, "w": "Маленький", "rd": "Malen'kiy", "m": "Kichkina", "g": "Adjective", "e": "Маленькая машина."},
        {"r": 60, "w": "Новый", "rd": "Noviy", "m": "Yangi", "g": "Adjective", "e": "Новый телефон."},
        # ... (I will keep these for now as a core set)
    ]

    # --- ARABIC DATA (Restored & High Quality) ---
    AR_DATA = [
        {"r": 1, "w": "السَّلَامُ عَلَيْكُم", "rd": "As-salāmu ʿalaykum", "m": "Assalomu alaykum", "g": "Greeting", "e": "السَّلَامُ عَلَيْكُم!"},
        {"r": 2, "w": "مَرْحَبًا", "rd": "Marḥaban", "m": "Salom", "g": "Greeting", "e": "مَرْحَبًا!"},
        {"r": 3, "w": "شُكْرًا", "rd": "Shukran", "m": "Rahmat", "g": "Polite", "e": "شُكْرًا جَزِيلًا."},
        {"r": 4, "w": "نَعَمْ", "rd": "Naʿam", "m": "Ha", "g": "Particle", "e": "نَعَمْ، صَحِيحٌ."},
        {"r": 5, "w": "لَا", "rd": "Lā", "m": "Yo'q", "g": "Particle", "e": "لَا، شُكْرًا."},
        {"r": 11, "w": "كِتَابٌ", "rd": "Kitābun", "m": "Kitob", "g": "Noun", "e": "هَذَا كِتَابٌ."},
        {"r": 12, "w": "قَلَمٌ", "rd": "Qalamun", "m": "Qalam", "g": "Noun", "e": "أَكْتُبُ بِالقَلَمِ."},
        {"r": 13, "w": "بَيْتٌ", "rd": "Baytun", "m": "Uy", "g": "Noun", "e": "بَيْتِي كَبِيرٌ."},
        {"r": 15, "w": "أَبٌ", "rd": "Abun", "m": "Ota", "g": "Noun", "e": "أَبِي رَجُلٌ طَيِّبٌ."},
        {"r": 16, "w": "أُمٌّ", "rd": "Ummun", "m": "Ona", "g": "Noun", "e": "أُمِّي فِي البَيْتِ."},
        {"r": 301, "w": "رَأْسٌ", "rd": "Raʾsun", "m": "Bosh", "g": "Noun", "e": "عِنْدِي صُدَاعٌ فِي رَأْسِي."},
        {"r": 302, "w": "عَيْنٌ", "rd": "ʿAynun", "m": "Ko'z", "g": "Noun", "e": "العَيْنُ جَوْهَرَةٌ ثَمِينَةٌ."},
        {"r": 306, "w": "يَدٌ", "rd": "Yadun", "m": "Qol", "g": "Noun", "e": "أَغْسِلُ يَدِي بِالصَّابُونِ."},
        {"r": 307, "w": "رِجْلٌ", "rd": "Rijlun", "m": "Oyoq", "g": "Noun", "e": "أَمْشِي عَلَى رِجْلَيَّ."},
        {"r": 341, "w": "تُفَّاحٌ", "rd": "Tuffāḥun", "m": "Olma", "g": "Noun", "e": "التُّفَّاحُ لَذِيذٌ."},
        {"r": 342, "w": "مَوْزٌ", "rd": "Mawzun", "m": "Banan", "g": "Noun", "e": "أُحِبُّ أَكْلَ المَوْزِ."},
        {"r": 451, "w": "طَبِيبٌ", "rd": "Ṭabībun", "m": "Shifokor", "g": "Noun", "e": "الطَّبِيبُ يُعَالِجُ المَرْضَى."},
        {"r": 453, "w": "مُعَلِّمٌ", "rd": "Muʿallimun", "m": "O'qituvchi", "g": "Noun", "e": "المُعَلِّمُ يَشْرَحُ الدَّرْسَ."},
    ]

    for item in RU_DATA:
        cur.execute("""INSERT OR REPLACE INTO word_library (word, lang, reading, meaning, grammar, example, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (item['w'], "ru", item['rd'], item['m'], item['g'], item.get('e',''), item['r']))
        
    for item in AR_DATA:
        cur.execute("""INSERT OR REPLACE INTO word_library (word, lang, reading, meaning, grammar, example, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (item['w'], "ar", item['rd'], item['m'], item['g'], item.get('e',''), item['r']))
        
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
