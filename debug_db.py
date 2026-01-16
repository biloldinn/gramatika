import sqlite3
db = sqlite3.connect("bot.db")
cur = db.cursor()

print("--- WORD LIBRARY COUNTS ---")
cur.execute("SELECT lang, COUNT(*) FROM word_library GROUP BY lang")
print(cur.fetchall())

print("\n--- SAMPLE ARABIC ---")
cur.execute("SELECT * FROM word_library WHERE lang='ar' LIMIT 5")
for r in cur.fetchall():
    print(r)

print("\n--- SAMPLE RUSSIAN ---")
cur.execute("SELECT * FROM word_library WHERE lang='ru' LIMIT 5")
for r in cur.fetchall():
    print(r) 
