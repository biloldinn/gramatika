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
    
    # ---------------------------------------------------------
    # RUSSIAN CURRICULUM (1-40)
    # ---------------------------------------------------------
    RU_DATA = [
        {"r": 1, "w": "Здравствуйте", "rd": "Zdravstvuyte", "m": "Assalomu alaykum", "g": "Formal greeting", "e": "Здравствуйте, меня зовут Али."},
        {"r": 2, "w": "Привет", "rd": "Privet", "m": "Salom", "g": "Informal greeting", "e": "Привет, друг!"},
        {"r": 3, "w": "Как вас зовут?", "rd": "Kak vas zovut?", "m": "Ismingiz nima?", "g": "Question", "e": "Скажите, как вас зовут?"},
        {"r": 4, "w": "Меня зовут...", "rd": "Menya zovut...", "m": "Mening ismim...", "g": "Phrase", "e": "Меня зовут Боб."},
        {"r": 5, "w": "Очень приятно", "rd": "Ochen' priyatno", "m": "Tanishganimdan xursandman", "g": "Phrase", "e": "Мне очень приятно."},
        {"r": 6, "w": "Как дела?", "rd": "Kak dela?", "m": "Ishlar qalay?", "g": "Question", "e": "Привет, как дела?"},
        {"r": 7, "w": "Хорошо", "rd": "Khorosho", "m": "Yaxshi", "g": "Adverb", "e": "Всё хорошо."},
        {"r": 8, "w": "Спасибо", "rd": "Spasibo", "m": "Rahmat", "g": "Polite", "e": "Спасибо большое."},
        {"r": 9, "w": "Пожалуйста", "rd": "Pozhaluysta", "m": "Iltimos / Arzimaydi", "g": "Polite", "e": "Пожалуйста, возьми."},
        {"r": 10, "w": "Да", "rd": "Da", "m": "Ha", "g": "Particle", "e": "Да, конечно."},
        {"r": 11, "w": "Нет", "rd": "Net", "m": "Yo'q", "g": "Particle", "e": "Нет, спасибо."},
        {"r": 12, "w": "До свидания", "rd": "Do svidaniya", "m": "Xayr", "g": "Farewell", "e": "Всем до свидания."},
        {"r": 13, "w": "Я", "rd": "Ya", "m": "Men", "g": "Pronoun", "e": "Я студент."},
        {"r": 14, "w": "Ты", "rd": "Ty", "m": "Sen", "g": "Pronoun", "e": "Ты врач?"},
        {"r": 15, "w": "Вы", "rd": "Vy", "m": "Siz", "g": "Pronoun", "e": "Кто вы?"},
        {"r": 16, "w": "Он", "rd": "On", "m": "U (erkak)", "g": "Pronoun", "e": "Он работает."},
        {"r": 17, "w": "Она", "rd": "Ona", "m": "U (ayol)", "g": "Pronoun", "e": "Она читает."},
        {"r": 18, "w": "Мы", "rd": "My", "m": "Biz", "g": "Pronoun", "e": "Мы друзья."},
        {"r": 19, "w": "Они", "rd": "Oni", "m": "Ular", "g": "Pronoun", "e": "Они здесь."},
        {"r": 20, "w": "Семья", "rd": "Sem'ya", "m": "Oila", "g": "Noun", "e": "Моя семья."},
        {"r": 21, "w": "Папа", "rd": "Papa", "m": "Dada", "g": "Noun", "e": "Папа дома."},
        {"r": 22, "w": "Мама", "rd": "Mama", "m": "Oyi", "g": "Noun", "e": "Мама добрая."},
        {"r": 23, "w": "Брат", "rd": "Brat", "m": "Aka/Uka", "g": "Noun", "e": "Мой брат."},
        {"r": 24, "w": "Сестра", "rd": "Sestra", "m": "Opa/Singil", "g": "Noun", "e": "Твоя сестра."},
        {"r": 25, "w": "Что", "rd": "Chto", "m": "Nima", "g": "Question", "e": "Что это?"},
        {"r": 26, "w": "Кто", "rd": "Kto", "m": "Kim", "g": "Question", "e": "Кто это?"},
        {"r": 27, "w": "Где", "rd": "Gde", "m": "Qayerda", "g": "Question", "e": "Где ты?"},
        {"r": 28, "w": "Когда", "rd": "Kogda", "m": "Qachon", "g": "Question", "e": "Когда урок?"},
        {"r": 29, "w": "Почему", "rd": "Pochemu", "m": "Nega", "g": "Question", "e": "Почему нет?"},
        {"r": 30, "w": "Как", "rd": "Kak", "m": "Qanday", "g": "Question", "e": "Как дела?"},
        {"r": 31, "w": "Быть", "rd": "Byt'", "m": "Bo'lmoq", "g": "Verb", "e": "Быть или не быть?"},
        {"r": 32, "w": "Делать", "rd": "Delat'", "m": "Qilmoq", "g": "Verb", "e": "Что делать?"},
        {"r": 33, "w": "Знать", "rd": "Znat'", "m": "Bilmoq", "g": "Verb", "e": "Я знаю."},
        {"r": 34, "w": "Понимать", "rd": "Ponimat'", "m": "Tushunmoq", "g": "Verb", "e": "Я понимаю."},
        {"r": 35, "w": "Говорить", "rd": "Govorit'", "m": "Gapirmoq", "g": "Verb", "e": "Говорите громче."},
        {"r": 36, "w": "Слушать", "rd": "Slushat'", "m": "Tinglamoq", "g": "Verb", "e": "Слушай меня."},
        {"r": 37, "w": "Читать", "rd": "Chitat'", "m": "O'qimoq", "g": "Verb", "e": "Я читаю книгу."},
        {"r": 38, "w": "Писать", "rd": "Pisat'", "m": "Yozmoq", "g": "Verb", "e": "Он пишет письмо."},
        {"r": 39, "w": "Идти", "rd": "Idti", "m": "Bormoq (piyoda)", "g": "Verb", "e": "Я иду домой."},
        {"r": 40, "w": "Ехать", "rd": "Yekhat'", "m": "Bormoq (transportda)", "g": "Verb", "e": "Мы едем в город."},
    ]

    # ---------------------------------------------------------
    # ARABIC CURRICULUM (1-40) - VOWELIZED (TASHKEEL)
    # ---------------------------------------------------------
    AR_DATA = [
        {"r": 1, "w": "السَّلَامُ عَلَيْكُم", "rd": "As-salāmu ʿalaykum", "m": "Assalomu alaykum", "g": "Greeting", "e": "السَّلَامُ عَلَيْكُم يَا صَدِيقِي"},
        {"r": 2, "w": "وَعَلَيْكُمُ السَّلَام", "rd": "Wa ʿalaykumu s-salām", "m": "Va alaykum assalom", "g": "Reply", "e": "وَعَلَيْكُمُ السَّلَام وَرَحْمَةُ اللهِ"},
        {"r": 3, "w": "مَرْحَبًا", "rd": "Marḥaban", "m": "Salom", "g": "Greeting", "e": "مَرْحَبًا بِكَ"},
        {"r": 4, "w": "أَهْلًا وَسَهْلًا", "rd": "Ahlan wa sahlan", "m": "Xush kelibsiz", "g": "Greeting", "e": "أَهْلًا وَسَهْلًا يَا أَخِي"},
        {"r": 5, "w": "مَا اسْمُكَ؟", "rd": "Mā ismuka?", "m": "Ismingiz nima? (erkak)", "g": "Question", "e": "مَا اسْمُكَ يَا وَلَدُ؟"},
        {"r": 6, "w": "اِسْمِي...", "rd": "Ismī...", "m": "Mening ismim...", "g": "Phrase", "e": "اِسْمِي مُحَمَّدٌ."},
        {"r": 7, "w": "كَيْفَ حَالُكَ؟", "rd": "Kayfa ḥāluka?", "m": "Ahvolingiz qanday?", "g": "Question", "e": "كَيْفَ حَالُكَ اليَوْمَ؟"},
        {"r": 8, "w": "بِخَيْر", "rd": "Bi-khayr", "m": "Yaxshi", "g": "Answer", "e": "أَنَا بِخَيْر الحَمْدُ للهِ."},
        {"r": 9, "w": "شُكْرًا", "rd": "Shukran", "m": "Rahmat", "g": "Polite", "e": "شُكْرًا جَزِيلًا."},
        {"r": 10, "w": "عَفْوًا", "rd": "ʿAfwan", "m": "Arzimaydi", "g": "Polite", "e": "عَفْوًا يَا سَيِّدِي."},
        {"r": 11, "w": "مِنْ أَيْنَ أَنْتَ؟", "rd": "Min ayna anta?", "m": "Siz qayerdansiz?", "g": "Question", "e": "مِنْ أَيْنَ أَنْتَ يَا طَالِبُ؟"},
        {"r": 12, "w": "أَنَا مِنْ...", "rd": "Anā min...", "m": "Men ...danman", "g": "Phrase", "e": "أَنَا مِنْ أُوزْبِكِسْتَان."},
        {"r": 13, "w": "إِلَى اللِّقَاء", "rd": "Ilā l-liqāʾ", "m": "Ko'rishguncha", "g": "Farewell", "e": "إِلَى اللِّقَاء قَرِيبًا."},
        {"r": 14, "w": "مَعَ السَّلَامَة", "rd": "Maʿa s-salāma", "m": "Omon bo'ling (hayr)", "g": "Farewell", "e": "مَعَ السَّلَامَة."},
        {"r": 15, "w": "نَعَمْ", "rd": "Naʿam", "m": "Ha", "g": "Particle", "e": "نَعَمْ، هَذَا صَحِيحٌ."},
        {"r": 16, "w": "لَا", "rd": "Lā", "m": "Yo'q", "g": "Particle", "e": "لَا، لَسْتُ طَبِيبًا."},
        {"r": 17, "w": "أَنَا", "rd": "Anā", "m": "Men", "g": "Pronoun", "e": "أَنَا مُعَلِّمٌ."},
        {"r": 18, "w": "أَنْتَ", "rd": "Anta", "m": "Sen (erkak)", "g": "Pronoun", "e": "أَنْتَ صَدِيقِي."},
        {"r": 19, "w": "أَنْتِ", "rd": "Anti", "m": "Sen (ayol)", "g": "Pronoun", "e": "أَنْتِ ذَكِيَّةٌ."},
        {"r": 20, "w": "هُوَ", "rd": "Huwa", "m": "U (erkak)", "g": "Pronoun", "e": "هُوَ فِي البَيْتِ."},
        {"r": 21, "w": "هِيَ", "rd": "Hiya", "m": "U (ayol)", "g": "Pronoun", "e": "هِيَ تَقْرَأُ."},
        {"r": 22, "w": "نَحْنُ", "rd": "Naḥnu", "m": "Biz", "g": "Pronoun", "e": "نَحْنُ طُلَّابٌ."},
        {"r": 23, "w": "مَنْ", "rd": "Man", "m": "Kim", "g": "Question", "e": "مَنْ هَذَا الرَّجُلُ؟"},
        {"r": 24, "w": "مَا", "rd": "Mā", "m": "Nima", "g": "Question", "e": "مَا اسْمُ هَذَا؟"},
        {"r": 25, "w": "أَيْنَ", "rd": "Ayna", "m": "Qayerda", "g": "Question", "e": "أَيْنَ الكِتَابُ؟"},
        {"r": 26, "w": "كِتَابٌ", "rd": "Kitābun", "m": "Kitob", "g": "Noun", "e": "هَذَا كِتَابٌ جَمِيلٌ."},
        {"r": 27, "w": "قَلَمٌ", "rd": "Qalamun", "m": "Qalam", "g": "Noun", "e": "عِنْدِي قَلَمٌ أَحْمَرُ."},
        {"r": 28, "w": "بَيْتٌ", "rd": "Baytun", "m": "Uy", "g": "Noun", "e": "بَيْتِي كَبِيرٌ."},
        {"r": 29, "w": "مَدْرَسَةٌ", "rd": "Madrasatun", "m": "Maktab", "g": "Noun", "e": "أَذْهَبُ إِلَى الْمَدْرَسَةِ."},
        {"r": 30, "w": "أَبٌ", "rd": "Abun", "m": "Ota", "g": "Noun", "e": "أَبِي يَعْمَلُ."},
        {"r": 31, "w": "أُمٌّ", "rd": "Ummun", "m": "Ona", "g": "Noun", "e": "أُمِّي فِي المَطْبَخِ."},
        {"r": 32, "w": "أَخٌ", "rd": "Akhun", "m": "Aka/Uka", "g": "Noun", "e": "لِي أَخٌ صَغِيرٌ."},
        {"r": 33, "w": "أُخْتٌ", "rd": "Ukhtun", "m": "Opa/Singil", "g": "Noun", "e": "هَذِهِ أُخْتِي."},
        {"r": 34, "w": "كَبِيرٌ", "rd": "Kabīrun", "m": "Katta", "g": "Adjective", "e": "الْفِيلُ كَبِيرٌ."},
        {"r": 35, "w": "صَغِيرٌ", "rd": "Ṣaghīrun", "m": "Kichik", "g": "Adjective", "e": "الْقِطُّ صَغِيرٌ."},
        {"r": 36, "w": "جَمِيلٌ", "rd": "Jamīlun", "m": "Chiroyli", "g": "Adjective", "e": "الْبُسْتَانُ جَمِيلٌ."},
        {"r": 37, "w": "جَدِيدٌ", "rd": "Jadīdun", "m": "Yangi", "g": "Adjective", "e": "ثَوْبٌ جَدِيدٌ."},
        {"r": 38, "w": "قَدِيمٌ", "rd": "Qadīmun", "m": "Eski", "g": "Adjective", "e": "بَيْتٌ قَدِيمٌ."},
        {"r": 39, "w": "وَاحِدٌ", "rd": "Wāḥidun", "m": "Bir (1)", "g": "Number", "e": "إِلَهٌ وَاحِدٌ."},
        {"r": 40, "w": "كَتَبَ", "rd": "Kataba", "m": "Yozdi", "g": "Verb", "e": "كَتَبَ الطَّالِبُ الدَّرْسَ."},
    ]

    count = 0
    for item in RU_DATA:
        cur.execute("""INSERT OR REPLACE INTO word_library (word, lang, reading, meaning, grammar, example, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (item['w'], "ru", item['rd'], item['m'], item['g'], item['e'], item['r']))
        count += 1
        
    for item in AR_DATA:
        cur.execute("""INSERT OR REPLACE INTO word_library (word, lang, reading, meaning, grammar, example, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (item['w'], "ar", item['rd'], item['m'], item['g'], item['e'], item['r']))
        count += 1
        
    db.commit()
    print(f"Seeding completed. Total operations: {count}")
    db.close()

if __name__ == "__main__":
    seed()
