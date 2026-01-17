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
    # RUSSIAN CURRICULUM (1-80)
    # ---------------------------------------------------------
    RU_DATA = [
        # ... (1-60 kept from previous) ...
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
        {"r": 16, "w": "Что", "rd": "Chto", "m": "Nima", "g": "Question", "e": "Что это?"},
        {"r": 17, "w": "Кто", "rd": "Kto", "m": "Kim", "g": "Question", "e": "Кто это?"},
        {"r": 18, "w": "Где", "rd": "Gde", "m": "Qayerda", "g": "Question", "e": "Где ты?"},
        {"r": 19, "w": "Когда", "rd": "Kogda", "m": "Qachon", "g": "Question", "e": "Когда?"},
        {"r": 20, "w": "Почему", "rd": "Pochemu", "m": "Nega", "g": "Question", "e": "Почему?"},
        {"r": 21, "w": "Дом", "rd": "Dom", "m": "Uy", "g": "Noun", "e": "Это мой дом."},
        {"r": 22, "w": "Школа", "rd": "Shkola", "m": "Maktab", "g": "Noun", "e": "Я иду в школу."},
        {"r": 23, "w": "Работа", "rd": "Rabota", "m": "Ish", "g": "Noun", "e": "Я на работе."},
        {"r": 24, "w": "Деньги", "rd": "Den'gi", "m": "Pul", "g": "Noun", "e": "У меня нет денег."},
        {"r": 25, "w": "Машина", "rd": "Mashina", "m": "Mashina", "g": "Noun", "e": "Это машина."},
        {"r": 26, "w": "Улица", "rd": "Ulitsa", "m": "Ko'cha", "g": "Noun", "e": "На улице."},
        {"r": 27, "w": "Город", "rd": "Gorod", "m": "Shahar", "g": "Noun", "e": "Красивый город."},
        {"r": 28, "w": "Друг", "rd": "Drug", "m": "Do'st", "g": "Noun", "e": "Мой друг."},
        {"r": 29, "w": "Время", "rd": "Vremya", "m": "Vaqt", "g": "Noun", "e": "Сколько времени?"},
        {"r": 30, "w": "Человек", "rd": "Chelovek", "m": "Odam", "g": "Noun", "e": "Один человек."},
        {"r": 31, "w": "Быть", "rd": "Byt'", "m": "Bo'lmoq", "g": "Verb", "e": "Я хочу быть там."},
        {"r": 32, "w": "Делать", "rd": "Delat'", "m": "Qilmoq", "g": "Verb", "e": "Что делать?"},
        {"r": 33, "w": "Знать", "rd": "Znat'", "m": "Bilmoq", "g": "Verb", "e": "Я не знаю."},
        {"r": 34, "w": "Думать", "rd": "Dumat'", "m": "O'ylamoq", "g": "Verb", "e": "Я думаю."},
        {"r": 35, "w": "Видеть", "rd": "Videt'", "m": "Ko'rmoq", "g": "Verb", "e": "Я вижу дом."},
        {"r": 36, "w": "Слышать", "rd": "Slyshat'", "m": "Eshitmoq", "g": "Verb", "e": "Я слышу тебя."},
        {"r": 37, "w": "Идти", "rd": "Idti", "m": "Bormoq", "g": "Verb", "e": "Я иду."},
        {"r": 38, "w": "Ехать", "rd": "Yekhat'", "m": "Bormoq (transp.)", "g": "Verb", "e": "Я еду на машине."},
        {"r": 39, "w": "Любить", "rd": "Lyubit'", "m": "Sevmoq", "g": "Verb", "e": "Я люблю тебя."},
        {"r": 40, "w": "Хотеть", "rd": "Khotet'", "m": "Xohlamoq", "g": "Verb", "e": "Я хочу есть."},
        {"r": 41, "w": "Вода", "rd": "Voda", "m": "Suv", "g": "Noun", "e": "Дайте воды."},
        {"r": 42, "w": "Хлеб", "rd": "Khleb", "m": "Non", "g": "Noun", "e": "Купи хлеб."},
        {"r": 43, "w": "Чай", "rd": "Chay", "m": "Choy", "g": "Noun", "e": "Зеленый чай."},
        {"r": 44, "w": "Кофе", "rd": "Kofe", "m": "Qahva", "g": "Noun", "e": "Черный кофе."},
        {"r": 45, "w": "Еда", "rd": "Yeda", "m": "Ovqat", "g": "Noun", "e": "Вкусная еда."},
        {"r": 46, "w": "Завтрак", "rd": "Zavtrak", "m": "Nonushta", "g": "Noun", "e": "Мой завтрак."},
        {"r": 47, "w": "Обед", "rd": "Obed", "m": "Tushlik", "g": "Noun", "e": "Пойдем на обед."},
        {"r": 48, "w": "Ужин", "rd": "Uzhin", "m": "Kechki ovqat", "g": "Noun", "e": "Скоро ужин."},
        {"r": 49, "w": "Сегодня", "rd": "Segodnya", "m": "Bugun", "g": "Adverb", "e": "Сегодня тепло."},
        {"r": 50, "w": "Завтра", "rd": "Zavtra", "m": "Ertaga", "g": "Adverb", "e": "Завтра увидимся."},
        {"r": 51, "w": "Вчера", "rd": "Vchera", "m": "Kecha", "g": "Adverb", "e": "Вчера был дождь."},
        {"r": 52, "w": "Утро", "rd": "Utro", "m": "Tong", "g": "Noun", "e": "Доброе утро."},
        {"r": 53, "w": "День", "rd": "Den'", "m": "Kun", "g": "Noun", "e": "Хороший день."},
        {"r": 54, "w": "Вечер", "rd": "Vecher", "m": "Kechqurun", "g": "Noun", "e": "Добрый вечер."},
        {"r": 55, "w": "Ночь", "rd": "Noch'", "m": "Tun", "g": "Noun", "e": "Спокойной ночи."},
        {"r": 56, "w": "Час", "rd": "Chas", "m": "Soat", "g": "Noun", "e": "Сейчас один час."},
        {"r": 57, "w": "Минута", "rd": "Minuta", "m": "Daqiqa", "g": "Noun", "e": "Одна минута."},
        {"r": 58, "w": "Большой", "rd": "Bol'shoy", "m": "Katta", "g": "Adjective", "e": "Большой дом."},
        {"r": 59, "w": "Маленький", "rd": "Malen'kiy", "m": "Kichkina", "g": "Adjective", "e": "Маленькая машина."},
        {"r": 60, "w": "Новый", "rd": "Noviy", "m": "Yangi", "g": "Adjective", "e": "Новый телефон."},
        
        # --- NEW (61-80) ---
        {"r": 61, "w": "Природа", "rd": "Priroda", "m": "Tabiat", "g": "Noun", "e": "Красивая природа."},
        {"r": 62, "w": "Дерево", "rd": "Derevo", "m": "Daraxt", "g": "Noun", "e": "Зеленое дерево."},
        {"r": 63, "w": "Цветок", "rd": "Tsvetok", "m": "Gul", "g": "Noun", "e": "Красный цветок."},
        {"r": 64, "w": "Солнце", "rd": "Solntse", "m": "Quyosh", "g": "Noun", "e": "Солнце светит."},
        {"r": 65, "w": "Луна", "rd": "Luna", "m": "Oy", "g": "Noun", "e": "Ясная луна."},
        {"r": 66, "w": "Небо", "rd": "Nebo", "m": "Osmon", "g": "Noun", "e": "Голубое небо."},
        {"r": 67, "w": "Море", "rd": "More", "m": "Dengiz", "g": "Noun", "e": "Синее море."},
        {"r": 68, "w": "Гора", "rd": "Gora", "m": "Tog'", "g": "Noun", "e": "Высокая гора."},
        {"r": 69, "w": "Лес", "rd": "Les", "m": "O'rmon", "g": "Noun", "e": "Густой лес."},
        {"r": 70, "w": "Помощь", "rd": "Pomoshch'", "m": "Yordam", "g": "Noun", "e": "Мне нужна помощь."},
        {"r": 71, "w": "Понимать", "rd": "Ponimat'", "m": "Tushunmoq", "g": "Verb", "e": "Я понимаю."},
        {"r": 72, "w": "Ждать", "rd": "Zhdat'", "m": "Kutmoq", "g": "Verb", "e": "Я жду тебя."},
        {"r": 73, "w": "Опасно", "rd": "Opasno", "m": "Xavfli", "g": "Adverb/Adj", "e": "Это опасно."},
        {"r": 74, "w": "Быстро", "rd": "Bystro", "m": "Tez", "g": "Adverb", "e": "Иди быстро."},
        {"r": 75, "w": "Медленно", "rd": "Medlenno", "m": "Sekin", "g": "Adverb", "e": "Говорите медленно."},
        {"r": 76, "w": "Окно", "rd": "Okno", "m": "Deraza", "g": "Noun", "e": "Открой окно."},
        {"r": 77, "w": "Дверь", "rd": "Dver'", "m": "Eshik", "g": "Noun", "e": "Закрой дверь."},
        {"r": 78, "w": "Книга", "rd": "Kniga", "m": "Kitob", "g": "Noun", "e": "Интересная книга."},
        {"r": 79, "w": "Письмо", "rd": "Pis'mo", "m": "Xat", "g": "Noun", "e": "Я пишу письмо."},
        {"r": 80, "w": "Язык", "rd": "Yazyk", "m": "Til", "g": "Noun", "e": "Русский язык."},
    ]

    # ---------------------------------------------------------
    # ARABIC CURRICULUM (1-80)
    # ---------------------------------------------------------
    AR_DATA = [
        # ... (1-60 kept from previous) ...
        {"r": 1, "w": "السَّلَامُ عَلَيْكُم", "rd": "As-salāmu ʿalaykum", "m": "Assalomu alaykum", "g": "Greeting", "e": "السَّلَامُ عَلَيْكُم!"},
        {"r": 2, "w": "مَرْحَبًا", "rd": "Marḥaban", "m": "Salom", "g": "Greeting", "e": "مَرْحَبًا!"},
        {"r": 3, "w": "شُكْرًا", "rd": "Shukran", "m": "Rahmat", "g": "Polite", "e": "شُكْرًا جَزِيلًا."},
        {"r": 4, "w": "نَعَمْ", "rd": "Naʿam", "m": "Ha", "g": "Particle", "e": "نَعَمْ، صَحِيحٌ."},
        {"r": 5, "w": "لَا", "rd": "Lā", "m": "Yo'q", "g": "Particle", "e": "لَا، شُكْرًا."},
        {"r": 6, "w": "كَيْفَ الْحَالُ؟", "rd": "Kayfa l-ḥāl?", "m": "Ahvolingiz qanday?", "g": "Question", "e": "كَيْفَ الْحَالُ؟"},
        {"r": 7, "w": "أَنَا", "rd": "Anā", "m": "Men", "g": "Pronoun", "e": "أَنَا هُنَا."},
        {"r": 8, "w": "أَنْتَ", "rd": "Anta", "m": "Sen (erkak)", "g": "Pronoun", "e": "مَنْ أَنْتَ؟"},
        {"r": 9, "w": "هُوَ", "rd": "Huwa", "m": "U (erkak)", "g": "Pronoun", "e": "هُوَ طَبِيبٌ."},
        {"r": 10, "w": "هِيَ", "rd": "Hiya", "m": "U (ayol)", "g": "Pronoun", "e": "هِيَ مُعَلِّمَةٌ."},
        {"r": 11, "w": "كِتَابٌ", "rd": "Kitābun", "m": "Kitob", "g": "Noun", "e": "هَذَا كِتَابٌ."},
        {"r": 12, "w": "قَلَمٌ", "rd": "Qalamun", "m": "Qalam", "g": "Noun", "e": "أَكْتُبُ بِالقَلَمِ."},
        {"r": 13, "w": "بَيْتٌ", "rd": "Baytun", "m": "Uy", "g": "Noun", "e": "بَيْتِي كَبِيرٌ."},
        {"r": 14, "w": "مَدْرَسَةٌ", "rd": "Madrasatun", "m": "Maktab", "g": "Noun", "e": "فِي المَدْرَسَةِ."},
        {"r": 15, "w": "أَبٌ", "rd": "Abun", "m": "Ota", "g": "Noun", "e": "أَبِي رَجُلٌ طَيِّبٌ."},
        {"r": 16, "w": "أُمٌّ", "rd": "Ummun", "m": "Ona", "g": "Noun", "e": "أُمِّي فِي البَيْتِ."},
        {"r": 17, "w": "أَخٌ", "rd": "Akhun", "m": "Aka/Uka", "g": "Noun", "e": "أَخِي الغَالِي."},
        {"r": 18, "w": "أُخْتٌ", "rd": "Ukhtun", "m": "Opa/Singil", "g": "Noun", "e": "هَذِهِ أُخْتِي."},
        {"r": 19, "w": "صَدِيقٌ", "rd": "Ṣadīqun", "m": "Do'st", "g": "Noun", "e": "هُوَ صَدِيقِي."},
        {"r": 20, "w": "اِسْمٌ", "rd": "Ismun", "m": "Ism", "g": "Noun", "e": "مَا اِسْمُكَ؟"},
        {"r": 21, "w": "مَا", "rd": "Mā", "m": "Nima", "g": "Question", "e": "مَا هَذَا؟"},
        {"r": 22, "w": "مَنْ", "rd": "Man", "m": "Kim", "g": "Question", "e": "مَنْ أَنْتَ؟"},
        {"r": 23, "w": "أَيْنَ", "rd": "Ayna", "m": "Qayerda", "g": "Question", "e": "أَيْنَ المَدْرَسَةُ؟"},
        {"r": 24, "w": "كَبِيرٌ", "rd": "Kabīrun", "m": "Katta", "g": "Adjective", "e": "بَيْتٌ كَبِيرٌ."},
        {"r": 25, "w": "صَغِيرٌ", "rd": "Ṣaghīrun", "m": "Kichik", "g": "Adjective", "e": "وَلَدٌ صَغِيرٌ."},
        {"r": 26, "w": "جَدِيدٌ", "rd": "Jadīdun", "m": "Yangi", "g": "Adjective", "e": "قَلَمٌ جَدِيدٌ."},
        {"r": 27, "w": "قَدِيمٌ", "rd": "Qadīmun", "m": "Eski", "g": "Adjective", "e": "كِتَابٌ قَدِيمٌ."},
        {"r": 28, "w": "جَمِيلٌ", "rd": "Jamīlun", "m": "Chiroyli", "g": "Adjective", "e": "بُسْتَانٌ جَمِيلٌ."},
        {"r": 29, "w": "كَتَبَ", "rd": "Kataba", "m": "Yozdi", "g": "Verb", "e": "كَتَبَ رِسَالَةً."},
        {"r": 30, "w": "قَرَأَ", "rd": "Qaraʾa", "m": "O'qidi", "g": "Verb", "e": "قَرَأَ الكِتَابَ."},
        {"r": 31, "w": "ذَهَبَ", "rd": "Dhahaba", "m": "Ketdi", "g": "Verb", "e": "ذَهَبَ إِلَى العَمَلِ."},
        {"r": 32, "w": "رَجَعَ", "rd": "Rajaʿa", "m": "Qaytdi", "g": "Verb", "e": "رَجَعَ إِلَى البَيْتِ."},
        {"r": 33, "w": "أَكَلَ", "rd": "Akala", "m": "Yedi", "g": "Verb", "e": "أَكَلَ التُّفَّاحَةَ."},
        {"r": 34, "w": "شَرِبَ", "rd": "Shariba", "m": "Ichdi", "g": "Verb", "e": "شَرِبَ المَاءَ."},
        {"r": 35, "w": "وَاحِدٌ", "rd": "Wāḥidun", "m": "Bir (1)", "g": "Number", "e": "وَلَدٌ وَاحِدٌ."},
        {"r": 36, "w": "اِثْنَانِ", "rd": "Ithnāni", "m": "Ikki (2)", "g": "Number", "e": "قَلَمَانِ اِثْنَانِ."},
        {"r": 37, "w": "ثَلَاثَةٌ", "rd": "Thalāthatun", "m": "Uch (3)", "g": "Number", "e": "ثَلَاثَةُ كُتُبٍ."},
        {"r": 38, "w": "أَرْبَعَةٌ", "rd": "Arbaʿatun", "m": "To'rt (4)", "g": "Number", "e": "أَرْبَعَةُ رِجَالٍ."},
        {"r": 39, "w": "خَمْسَةٌ", "rd": "Khamsatun", "m": "Besh (5)", "g": "Number", "e": "خَمْسَةُ أَيَّامٍ."},
        {"r": 40, "w": "عَشَرَةٌ", "rd": "ʿAsharatun", "m": "O'n (10)", "g": "Number", "e": "عَشَرَةُ دَنَانِيرَ."},
        {"r": 41, "w": "مَاءٌ", "rd": "Māʾun", "m": "Suv", "g": "Noun", "e": "أُرِيدُ مَاءً."},
        {"r": 42, "w": "خُبْزٌ", "rd": "Khubzun", "m": "Non", "g": "Noun", "e": "آكُلُ الخُبْزَ."},
        {"r": 43, "w": "شَايٌ", "rd": "Shāyun", "m": "Choy", "g": "Noun", "e": "أَشْرَبُ الشَّايَ."},
        {"r": 44, "w": "قَهْوَةٌ", "rd": "Qahwatun", "m": "Qahva", "g": "Noun", "e": "أُحِبُّ القَهْوَةَ."},
        {"r": 45, "w": "طَعَامٌ", "rd": "Ṭaʿāmun", "m": "Ovqat", "g": "Noun", "e": "الطَّعَامُ لَذِيذٌ."},
        {"r": 46, "w": "تُفَّاحَةٌ", "rd": "Tuffāḥatun", "m": "Olma", "g": "Noun", "e": "تُفَّاحَةٌ حَمْرَاءُ."},
        {"r": 47, "w": "لَحْمٌ", "rd": "Laḥmun", "m": "Go'sht", "g": "Noun", "e": "لَحْمٌ مَشْوِيٌّ."},
        {"r": 48, "w": "حَلِيبٌ", "rd": "Ḥalībun", "m": "Sut", "g": "Noun", "e": "حَلِيبٌ طَازَجٌ."},
        {"r": 49, "w": "يَوْمٌ", "rd": "Yawmun", "m": "Kun", "g": "Noun", "e": "كُلَّ يَوْمٍ."},
        {"r": 50, "w": "لَيْلَةٌ", "rd": "Laylatun", "m": "Tun", "g": "Noun", "e": "لَيْلَةٌ سَعِيدَةٌ."},
        {"r": 51, "w": "صَبَاحٌ", "rd": "Ṣabāḥun", "m": "Tong", "g": "Noun", "e": "صَبَاحُ الخَيْرِ."},
        {"r": 52, "w": "مَسَاءٌ", "rd": "Masāʾun", "m": "Kechqurun", "g": "Noun", "e": "مَسَاءُ النُّورِ."},
        {"r": 53, "w": "سَاعَةٌ", "rd": "Sāʿatun", "m": "Soat", "g": "Noun", "e": "كَمِ السَّاعَةُ؟"},
        {"r": 54, "w": "دَقِيقَةٌ", "rd": "Daqīqatun", "m": "Daqiqa", "g": "Noun", "e": "خَمْسُ دَقَائِقَ."},
        {"r": 55, "w": "اليَوْمَ", "rd": "Al-yawma", "m": "Bugun", "g": "Adverb", "e": "اليَوْمَ حَارٌّ."},
        {"r": 56, "w": "غَدًا", "rd": "Ghadan", "m": "Ertaga", "g": "Adverb", "e": "أَرَاكَ غَدًا."},
        {"r": 57, "w": "أَمْسِ", "rd": "Amsi", "m": "Kecha", "g": "Adverb", "e": "ذَهَبْتُ أَمْسِ."},
        {"r": 58, "w": "سَيَّارَةٌ", "rd": "Sayyāratun", "m": "Mashina", "g": "Noun", "e": "سَيَّارَةٌ جَدِيدَةٌ."},
        {"r": 59, "w": "طَرِيقٌ", "rd": "Ṭarīqun", "m": "Yo'l", "g": "Noun", "e": "الطَّرِيقُ طَوِيلٌ."},
        {"r": 60, "w": "سُوقٌ", "rd": "Sūqun", "m": "Bozor", "g": "Noun", "e": "فِي السُّوقِ."},
        
        # --- NEW (61-80) ---
        {"r": 61, "w": "طَبِيعَةٌ", "rd": "Ṭabīʿatun", "m": "Tabiat", "g": "Noun", "e": "الطَّبِيعَةُ سَاحِرَةٌ."},
        {"r": 62, "w": "شَجَرَةٌ", "rd": "Shajaratun", "m": "Daraxt", "g": "Noun", "e": "هَذِهِ شَجَرَةٌ كَبِيرَةٌ."},
        {"r": 63, "w": "زَهْرَةٌ", "rd": "Zahratun", "m": "Gul", "g": "Noun", "e": "زَهْرَةٌ جَمِيلَةٌ."},
        {"r": 64, "w": "شَمْسٌ", "rd": "Shamsun", "m": "Quyosh", "g": "Noun", "e": "الشَّمْسُ مُشْرِقَةٌ."},
        {"r": 65, "w": "قَمَرٌ", "rd": "Qamarun", "m": "Oy", "g": "Noun", "e": "القَمَرُ طَالِعٌ."},
        {"r": 66, "w": "سَمَاءٌ", "rd": "Samāʾun", "m": "Osmon", "g": "Noun", "e": "السَّمَاءُ صَافِيَةٌ."},
        {"r": 67, "w": "بَحْرٌ", "rd": "Baḥrun", "m": "Dengiz", "g": "Noun", "e": "البَحْرُ وَاسِعٌ."},
        {"r": 68, "w": "جَبَلٌ", "rd": "Jabalun", "m": "Tog'", "g": "Noun", "e": "جَبَلٌ عَالٍ."},
        {"r": 69, "w": "غَابَةٌ", "rd": "Ghabatun", "m": "O'rmon", "g": "Noun", "e": "غَابَةٌ خَضْرَاءُ."},
        {"r": 70, "w": "مُسَاعَدَةٌ", "rd": "Musāʿadatun", "m": "Yordam", "g": "Noun", "e": "أُرِيدُ مُسَاعَدَةً."},
        {"r": 71, "w": "فَهِمَ", "rd": "Fahima", "m": "Tushundi", "g": "Verb", "e": "فَهِمْتُ الدَّرْسَ."},
        {"r": 72, "w": "انْتَظَرَ", "rd": "Intaẓara", "m": "Kutdi", "g": "Verb", "e": "انْتَظَرْتُكَ طَوِيلًا."},
        {"r": 73, "w": "خَطَرٌ", "rd": "Khaṭarun", "m": "Xavf", "g": "Noun", "e": "هَذَا خَطَرٌ."},
        {"r": 74, "w": "بِسُرْعَةٍ", "rd": "Bi-surʿatin", "m": "Tezda", "g": "Adverb", "e": "تَعَالَ بِسُرْعَةٍ."},
        {"r": 75, "w": "بِبُطْءٍ", "rd": "Bi-buṭʾin", "m": "Sekin", "g": "Adverb", "e": "تَكَلَّمْ بِبُطْءٍ."},
        {"r": 76, "w": "نَافِذَةٌ", "rd": "Nāfidhatun", "m": "Deraza", "g": "Noun", "e": "اِفْتَحِ النَّافِذَةَ."},
        {"r": 77, "w": "بَابٌ", "rd": "Bābun", "m": "Eshik", "g": "Noun", "e": "اُغْلِقِ البَابَ."},
        {"r": 78, "w": "كِتَابٌ", "rd": "Kitābun", "m": "Kitob", "g": "Noun", "e": "قَرَأْتُ كِتَابًا."},
        {"r": 79, "w": "رِسَالَةٌ", "rd": "Risālatun", "m": "Xat/Xabar", "g": "Noun", "e": "أَرْسَلْتُ رِسَالَةً."},
        {"r": 80, "w": "لُغَةٌ", "rd": "Lughatun", "m": "Til", "g": "Noun", "e": "اللُّغَةُ العَرَبِيَّةُ."},
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
