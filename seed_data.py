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
    # RUSSIAN CURRICULUM (1-60)
    # ---------------------------------------------------------
    RU_DATA = [
        # --- PREVIOUS (1-40) ---
        {"r": 1, "w": "Здравствуйте", "rd": "Zdravstvuyte", "m": "Assalomu alaykum", "g": "Greeting", "e": "Здравствуйте!"},
        {"r": 2, "w": "Привет", "rd": "Privet", "m": "Salom", "g": "Greeting", "e": "Привет, друг!"},
        {"r": 3, "w": "Как дела?", "rd": "Kak dela?", "m": "Ishlar qalay?", "g": "Question", "e": "Привет, как дела?"},
        {"r": 4, "w": "Спасибо", "rd": "Spasibo", "m": "Rahmat", "g": "Polite", "e": "Спасибо большое."},
        {"r": 5, "w": "Пожалуйста", "rd": "Pozhaluysta", "m": "Iltimos", "g": "Polite", "e": "Пожалуйста."},
        {"r": 6, "w": "Да", "rd": "Da", "m": "Ha", "g": "Particle", "e": "Да, я знаю."},
        {"r": 7, "w": "Нет", "rd": "Net", "m": "Yo'q", "g": "Particle", "e": "Нет, спасибо."},
        {"r": 8, "w": "Я", "rd": "Ya", "m": "Men", "g": "Pronoun", "e": "Я студент."},
        {"r": 9, "w": "Ты", "rd": "Ty", "m": "Sen", "g": "Pronoun", "e": "Ты где?"},
        {"r": 10, "w": "Хорошо", "rd": "Khorosho", "m": "Yaxshi", "g": "Adverb", "e": "Всё хорошо."},
        {"r": 11, "w": "Семья", "rd": "Sem'ya", "m": "Oila", "g": "Noun", "e": "Моя семья."},
        {"r": 12, "w": "Папа", "rd": "Papa", "m": "Dada", "g": "Noun", "e": "Папа дома."},
        {"r": 13, "w": "Мама", "rd": "Mama", "m": "Oyi", "g": "Noun", "e": "Мама готовит."},
        {"r": 14, "w": "Брат", "rd": "Brat", "m": "Aka/Uka", "g": "Noun", "e": "Мой брат."},
        {"r": 15, "w": "Сестра", "rd": "Sestra", "m": "Opa/Singil", "g": "Noun", "e": "Твоя сестра."},
        {"r": 16, "w": "Что", "rd": "Chto", "m": "Nima", "g": "Question", "e": "Что это?"},
        {"r": 17, "w": "Кто", "rd": "Kto", "m": "Kim", "g": "Question", "e": "Кто это?"},
        {"r": 18, "w": "Где", "rd": "Gde", "m": "Qayerda", "g": "Question", "e": "Где ты?"},
        {"r": 19, "w": "Когда", "rd": "Kogda", "m": "Qachon", "g": "Question", "e": "Когда?"},
        {"r": 20, "w": "Почему", "rd": "Pochemu", "m": "Nega", "g": "Question", "e": "Почему?"},
        {"r": 21, "w": "Дом", "rd": "Dom", "m": "Uy", "g": "Noun", "e": "Это мой дом."},
        {"r": 22, "w": "Школа", "rd": "Shkola", "m": "Maktab", "g": "Noun", "e": "Я иду в школу."},
        {"r": 23, "w": "Работа", "rd": "Rabota", "m": "Ish", "g": "Noun", "e": "У меня много работы."},
        {"r": 24, "w": "Деньги", "rd": "Den'gi", "m": "Pul", "g": "Noun", "e": "Где деньги?"},
        {"r": 25, "w": "Машина", "rd": "Mashina", "m": "Mashina", "g": "Noun", "e": "Новая машина."},
        {"r": 26, "w": "Улица", "rd": "Ulitsa", "m": "Ko'cha", "g": "Noun", "e": "На улице холодно."},
        {"r": 27, "w": "Город", "rd": "Gorod", "m": "Shahar", "g": "Noun", "e": "Большой город."},
        {"r": 28, "w": "Друг", "rd": "Drug", "m": "Do'st", "g": "Noun", "e": "Мой друг."},
        {"r": 29, "w": "Время", "rd": "Vremya", "m": "Vaqt", "g": "Noun", "e": "Нет времени."},
        {"r": 30, "w": "Человек", "rd": "Chelovek", "m": "Odam", "g": "Noun", "e": "Хороший человек."},
        {"r": 31, "w": "Быть", "rd": "Byt'", "m": "Bo'lmoq", "g": "Verb", "e": "Я хочу быть врачом."},
        {"r": 32, "w": "Делать", "rd": "Delat'", "m": "Qilmoq", "g": "Verb", "e": "Что ты делаешь?"},
        {"r": 33, "w": "Знать", "rd": "Znat'", "m": "Bilmoq", "g": "Verb", "e": "Я знаю."},
        {"r": 34, "w": "Думать", "rd": "Dumat'", "m": "O'ylamoq", "g": "Verb", "e": "Я думаю, да."},
        {"r": 35, "w": "Видеть", "rd": "Videt'", "m": "Ko'rmoq", "g": "Verb", "e": "Я вижу тебя."},
        {"r": 36, "w": "Слышать", "rd": "Slyshat'", "m": "Eshitmoq", "g": "Verb", "e": "Ты слышишь?"},
        {"r": 37, "w": "Идти", "rd": "Idti", "m": "Bormoq (piyoda)", "g": "Verb", "e": "Я иду."},
        {"r": 38, "w": "Ехать", "rd": "Yekhat'", "m": "Bormoq (transport)", "g": "Verb", "e": "Мы едем."},
        {"r": 39, "w": "Любить", "rd": "Lyubit'", "m": "Sevmoq/Yaxshi ko'rmoq", "g": "Verb", "e": "Я люблю спорт."},
        {"r": 40, "w": "Хотеть", "rd": "Khotet'", "m": "Xohlamoq", "g": "Verb", "e": "Я хочу спать."},

        # --- NEW TOPIC: FOOD & TIME (41-60) ---
        {"r": 41, "w": "Вода", "rd": "Voda", "m": "Suv", "g": "Noun", "e": "Дайте воды, пожалуйста."},
        {"r": 42, "w": "Хлеб", "rd": "Khleb", "m": "Non", "g": "Noun", "e": "Свежий хлеб."},
        {"r": 43, "w": "Чай", "rd": "Chay", "m": "Choy", "g": "Noun", "e": "Я буду чай."},
        {"r": 44, "w": "Кофе", "rd": "Kofe", "m": "Qahva", "g": "Noun", "e": "Горячий кофе."},
        {"r": 45, "w": "Еда", "rd": "Yeda", "m": "Ovqat", "g": "Noun", "e": "Вкусная еда."},
        {"r": 46, "w": "Завтрак", "rd": "Zavtrak", "m": "Nonushta", "g": "Noun", "e": "На завтрак яйца."},
        {"r": 47, "w": "Обед", "rd": "Obed", "m": "Tushlik", "g": "Noun", "e": "Пора на обед."},
        {"r": 48, "w": "Ужин", "rd": "Uzhin", "m": "Kechki ovqat", "g": "Noun", "e": "Что на ужин?"},
        {"r": 49, "w": "Сегодня", "rd": "Segodnya", "m": "Bugun", "g": "Adverb", "e": "Сегодня тепло."},
        {"r": 50, "w": "Завтра", "rd": "Zavtra", "m": "Ertaga", "g": "Adverb", "e": "Завтра увидимся."},
        {"r": 51, "w": "Вчера", "rd": "Vchera", "m": "Kecha", "g": "Adverb", "e": "Вчера был дождь."},
        {"r": 52, "w": "Утро", "rd": "Utro", "m": "Tong", "g": "Noun", "e": "Доброе утро."},
        {"r": 53, "w": "День", "rd": "Den'", "m": "Kun", "g": "Noun", "e": "Хороший день."},
        {"r": 54, "w": "Вечер", "rd": "Vecher", "m": "Kechqurun", "g": "Noun", "e": "Добрый вечер."},
        {"r": 55, "w": "Ночь", "rd": "Noch'", "m": "Tun", "g": "Noun", "e": "Спокойной ночи."},
        {"r": 56, "w": "Час", "rd": "Chas", "m": "Soat", "g": "Noun", "e": "Который час?"},
        {"r": 57, "w": "Минута", "rd": "Minuta", "m": "Daqiqa", "g": "Noun", "e": "Одна минута."},
        {"r": 58, "w": "Большой", "rd": "Bol'shoy", "m": "Katta", "g": "Adjective", "e": "Большой дом."},
        {"r": 59, "w": "Маленький", "rd": "Malen'kiy", "m": "Kichkina", "g": "Adjective", "e": "Маленький кот."},
        {"r": 60, "w": "Новый", "rd": "Noviy", "m": "Yangi", "g": "Adjective", "e": "Новый телефон."},
    ]

    # ---------------------------------------------------------
    # ARABIC CURRICULUM (1-60) - VOWELS
    # ---------------------------------------------------------
    AR_DATA = [
        # --- PREVIOUS (1-40) ---
        {"r": 1, "w": "السَّلَامُ عَلَيْكُم", "rd": "As-salāmu ʿalaykum", "m": "Assalomu alaykum", "g": "Greeting", "e": "السَّلَامُ عَلَيْكُم!"},
        {"r": 2, "w": "مَرْحَبًا", "rd": "Marḥaban", "m": "Salom", "g": "Greeting", "e": "مَرْحَبًا يَا صَدِيقِي."},
        {"r": 3, "w": "شُكْرًا", "rd": "Shukran", "m": "Rahmat", "g": "Polite", "e": "شُكْرًا جَزِيلًا."},
        {"r": 4, "w": "نَعَمْ", "rd": "Naʿam", "m": "Ha", "g": "Particle", "e": "نَعَمْ، صَحِيحٌ."},
        {"r": 5, "w": "لَا", "rd": "Lā", "m": "Yo'q", "g": "Particle", "e": "لَا، شُكْرًا."},
        {"r": 6, "w": "كَيْفَ الْحَالُ؟", "rd": "Kayfa l-ḥāl?", "m": "Ahvolingiz qanday?", "g": "Question", "e": "كَيْفَ الْحَالُ؟"},
        {"r": 7, "w": "أَنَا", "rd": "Anā", "m": "Men", "g": "Pronoun", "e": "أَنَا طَالِبٌ."},
        {"r": 8, "w": "أَنْتَ", "rd": "Anta", "m": "Sen (erkak)", "g": "Pronoun", "e": "أَنْتَ مُعَلِّمٌ."},
        {"r": 9, "w": "هُوَ", "rd": "Huwa", "m": "U (erkak)", "g": "Pronoun", "e": "هُوَ طَبِيبٌ."},
        {"r": 10, "w": "هِيَ", "rd": "Hiya", "m": "U (ayol)", "g": "Pronoun", "e": "هِيَ ذَكِيَّةٌ."},
        {"r": 11, "w": "كِتَابٌ", "rd": "Kitābun", "m": "Kitob", "g": "Noun", "e": "هَذَا كِتَابٌ."},
        {"r": 12, "w": "قَلَمٌ", "rd": "Qalamun", "m": "Qalam", "g": "Noun", "e": "أَكْتُبُ بِالقَلَمِ."},
        {"r": 13, "w": "بَيْتٌ", "rd": "Baytun", "m": "Uy", "g": "Noun", "e": "بَيْتِي جَمِيلٌ."},
        {"r": 14, "w": "مَدْرَسَةٌ", "rd": "Madrasatun", "m": "Maktab", "g": "Noun", "e": "ذَهَبْتُ إِلَى المَدْرَسَةِ."},
        {"r": 15, "w": "أَبٌ", "rd": "Abun", "m": "Ota", "g": "Noun", "e": "أَبِي رَجُلٌ طَيِّبٌ."},
        {"r": 16, "w": "أُمٌّ", "rd": "Ummun", "m": "Ona", "g": "Noun", "e": "أُمِّي تُطْبُخُ."},
        {"r": 17, "w": "أَخٌ", "rd": "Akhun", "m": "Aka/Uka", "g": "Noun", "e": "لِي أَخٌ وَاحِدٌ."},
        {"r": 18, "w": "أُخْتٌ", "rd": "Ukhtun", "m": "Opa/Singil", "g": "Noun", "e": "أُخْتِي صَغِيرَةٌ."},
        {"r": 19, "w": "صَدِيقٌ", "rd": "Ṣadīqun", "m": "Do'st", "g": "Noun", "e": "هُوَ صَدِيقِي."},
        {"r": 20, "w": "اِسْمٌ", "rd": "Ismun", "m": "Ism", "g": "Noun", "e": "مَا اِسْمُكَ؟"},
        {"r": 21, "w": "مَا", "rd": "Mā", "m": "Nima", "g": "Question", "e": "مَا هَذَا؟"},
        {"r": 22, "w": "مَنْ", "rd": "Man", "m": "Kim", "g": "Question", "e": "مَنْ أَنْتَ؟"},
        {"r": 23, "w": "أَيْنَ", "rd": "Ayna", "m": "Qayerda", "g": "Question", "e": "أَيْنَ البَيْتُ؟"},
        {"r": 24, "w": "كَبِيرٌ", "rd": "Kabīrun", "m": "Katta", "g": "Adjective", "e": "بَيْتٌ كَبِيرٌ."},
        {"r": 25, "w": "صَغِيرٌ", "rd": "Ṣaghīrun", "m": "Kichik", "g": "Adjective", "e": "وَلَدٌ صَغِيرٌ."},
        {"r": 26, "w": "جَدِيدٌ", "rd": "Jadīdun", "m": "Yangi", "g": "Adjective", "e": "قَلَمٌ جَدِيدٌ."},
        {"r": 27, "w": "قَدِيمٌ", "rd": "Qadīmun", "m": "Eski", "g": "Adjective", "e": "كِتَابٌ قَدِيمٌ."},
        {"r": 28, "w": "جَمِيلٌ", "rd": "Jamīlun", "m": "Chiroyli", "g": "Adjective", "e": "بُسْتَانٌ جَمِيلٌ."},
        {"r": 29, "w": "كَتَبَ", "rd": "Kataba", "m": "Yozdi", "g": "Verb", "e": "كَتَبَ الدَّرْسَ."},
        {"r": 30, "w": "قَرَأَ", "rd": "Qaraʾa", "m": "O'qidi", "g": "Verb", "e": "قَرَأَ القُرْآنَ."},
        {"r": 31, "w": "ذَهَبَ", "rd": "Dhahaba", "m": "Ketdi", "g": "Verb", "e": "ذَهَبَ إِلَى العَمَلِ."},
        {"r": 32, "w": "رَجَعَ", "rd": "Rajaʿa", "m": "Qaytdi", "g": "Verb", "e": "رَجَعَ مِنَ السَّفَرِ."},
        {"r": 33, "w": "أَكَلَ", "rd": "Akala", "m": "Yedi", "g": "Verb", "e": "أَكَلَ الخُبْزَ."},
        {"r": 34, "w": "شَرِبَ", "rd": "Shariba", "m": "Ichdi", "g": "Verb", "e": "شَرِبَ المَاءَ."},
        {"r": 35, "w": "وَاحِدٌ", "rd": "Wāḥidun", "m": "Bir (1)", "g": "Number", "e": "رَقَمُ وَاحِدٍ."},
        {"r": 36, "w": "اِثْنَانِ", "rd": "Ithnāni", "m": "Ikki (2)", "g": "Number", "e": "قَلَمَانِ اِثْنَانِ."},
        {"r": 37, "w": "ثَلَاثَةٌ", "rd": "Thalāthatun", "m": "Uch (3)", "g": "Number", "e": "ثَلَاثَةُ كُتُبٍ."},
        {"r": 38, "w": "أَرْبَعَةٌ", "rd": "Arbaʿatun", "m": "To'rt (4)", "g": "Number", "e": "أَرْبَعَةُ رِجَالٍ."},
        {"r": 39, "w": "خَمْسَةٌ", "rd": "Khamsatun", "m": "Besh (5)", "g": "Number", "e": "خَمْسَةُ أَيَّامٍ."},
        {"r": 40, "w": "عَشَرَةٌ", "rd": "ʿAsharatun", "m": "O'n (10)", "g": "Number", "e": "عَشَرَةُ دَنَانِيرَ."},
        
        # --- NEW TOPIC: FOOD & TIME (41-60) ---
        {"r": 41, "w": "مَاءٌ", "rd": "Māʾun", "m": "Suv", "g": "Noun", "e": "أُرِيدُ مَاءً بَارِدًا."},
        {"r": 42, "w": "خُبْزٌ", "rd": "Khubzun", "m": "Non", "g": "Noun", "e": "هَذَا خُبْزٌ حَارٌّ."},
        {"r": 43, "w": "شَايٌ", "rd": "Shāyun", "m": "Choy", "g": "Noun", "e": "شَايٌ بِالْحَلِيبِ."},
        {"r": 44, "w": "قَهْوَةٌ", "rd": "Qahwatun", "m": "Qahva", "g": "Noun", "e": "أُحِبُّ الْقَهْوَةَ."},
        {"r": 45, "w": "طَعَامٌ", "rd": "Ṭaʿāmun", "m": "Ovqat", "g": "Noun", "e": "الطَّعَامُ لَذِيذٌ."},
        {"r": 46, "w": "تُفَّاحَةٌ", "rd": "Tuffāḥatun", "m": "Olma", "g": "Noun", "e": "أَكَلْتُ تُفَّاحَةً."},
        {"r": 47, "w": "لَحْمٌ", "rd": "Laḥmun", "m": "Go'sht", "g": "Noun", "e": "لَحْمٌ مَشْوِيٌّ."},
        {"r": 48, "w": "حَلِيبٌ", "rd": "Ḥalībun", "m": "Sut", "g": "Noun", "e": "اشرب الحليب."},
        {"r": 49, "w": "يَوْمٌ", "rd": "Yawmun", "m": "Kun", "g": "Noun", "e": "كُلَّ يَوْمٍ."},
        {"r": 50, "w": "لَيْلَةٌ", "rd": "Laylatun", "m": "Tun", "g": "Noun", "e": "لَيْلَةٌ سَعِيدَةٌ."},
        {"r": 51, "w": "صَبَاحٌ", "rd": "Ṣabāḥun", "m": "Tong", "g": "Noun", "e": "صَبَاحُ الخَيْرِ."},
        {"r": 52, "w": "مَسَاءٌ", "rd": "Masāʾun", "m": "Kechqurun", "g": "Noun", "e": "مَسَاءُ النُّورِ."},
        {"r": 53, "w": "سَاعَةٌ", "rd": "Sāʿatun", "m": "Soat", "g": "Noun", "e": "كَمِ السَّاعَةُ؟"},
        {"r": 54, "w": "دَقِيقَةٌ", "rd": "Daqīqatun", "m": "Daqiqa", "g": "Noun", "e": "انْتَظِرْ دَقِيقَةً."},
        {"r": 55, "w": "اليَوْمَ", "rd": "Al-yawma", "m": "Bugun", "g": "Adverb", "e": "اليَوْمَ حَارٌّ."},
        {"r": 56, "w": "غَدًا", "rd": "Ghadan", "m": "Ertaga", "g": "Adverb", "e": "سَأَرَاكَ غَدًا."},
        {"r": 57, "w": "أَمْسِ", "rd": "Amsi", "m": "Kecha", "g": "Adverb", "e": "كُنْتُ هُنَا أَمْسِ."},
        {"r": 58, "w": "سَيَّارَةٌ", "rd": "Sayyāratun", "m": "Mashina", "g": "Noun", "e": "سَيَّارَةٌ سَرِيعَةٌ."},
        {"r": 59, "w": "طَرِيقٌ", "rd": "Ṭarīqun", "m": "Yo'l", "g": "Noun", "e": "هَذَا طَرِيقٌ طَوِيلٌ."},
        {"r": 60, "w": "سُوقٌ", "rd": "Sūqun", "m": "Bozor", "g": "Noun", "e": "أَذْهَبُ إِلَى السُّوقِ."},
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
