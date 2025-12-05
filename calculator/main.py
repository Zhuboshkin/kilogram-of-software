
def calc(x):
    # база чисел
    word_to_num = {
     "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
    "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
    "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
    "сто": 100, "двести": 200, "триста": 300, "четыреста": 400,
    "пятьсот": 500, "шестьсот": 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900,
    "тысяча": 1000, "тысячи": 1000, "тысяч": 1000,
    "миллион": 1_000_000, "миллиона": 1_000_000, "миллионов": 1_000_000,
    "миллиард": 1_000_000_000, "миллиарда": 1_000_000_000, "миллиардов": 1_000_000_000,
    "одна": 1,
    "две": 2
    }
    # база чисел (число -> слово)
    num_to_word = {
        0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
    6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
    11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
    16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
    20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят",
    60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
    100: "сто", 200: "двести", 300: "триста", 400: "четыреста",
    500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот",
    1000: "тысяча",
    1_000_000: "миллион",
    1_000_000_000: "миллиард"
    }

    # база знаков (слово -> символ операции)
    znak = {
        "плюс": "+",
        "минус": "-",
        "умножить": "*",
        "разделить": "/",
        "остаток": "%",
        "в степени": "**",
        'скобка открывается':'(',
        'скобка закрывается':')',
    }
    # словарь ошибок (код -> сообщение)
    error_messages = {
        "division_by_zero": "Деление на ноль",
        "unbalanced_brackets": "Несбалансированные скобки",
        "invalid_expression": "Некорректное выражение",
        "not_enough_operands": "Недостаточно операндов",
        "unknown_operation": "Неизвестная операция",
        "invalid_number": "Неправильная запись числа"
    }

    # словарь для преобразования дробных частей (разрядность -> форма слова)
    decimal_forms = {
    "десятая": 0.1, "десятых": 0.1,
    "сотая": 0.01, "сотых": 0.01,
    "тысячная": 0.001, "тысячных": 0.001,
    "миллионная": 0.000001, "миллионных": 0.000001,
    1: "десятых",
    2: "сотых",
    3: "тысячных",
    4: "десятитысячных",
    5: "стотысячных",
    6: "миллионных",
    7: "десятимиллионных",
    8: "стомиллионных"
    }
    def number_to_words(n):
        if n == 0:
            return "ноль"
        if n >= 1_000_000:
            return "один миллион" if n == 1_000_000 else "слишком большое число"

        def under_thousand(num):
            """Преобразует число до 999"""
            if num == 0:
                return ""
            if num < 20:
                return num_to_word.get(num, "")
            if num < 100:
                des = (num // 10) * 10
                ed = num % 10
                if ed == 0:
                    return num_to_word[des]
                return num_to_word[des] + " " + num_to_word[ed]
            # 100–999
            sot = (num // 100) * 100
            ostatok = num % 100
            if ostatok == 0:
                return num_to_word[sot]
            return num_to_word[sot] + " " + under_thousand(ostatok)

        # Разбиваем число на тысячи и остаток
        tys = n // 1000
        ostatok = n % 1000

        parts = []
        if tys > 0:
            tys_slovo = under_thousand(tys)
            # Склоняем "тысяча"
            if tys % 10 == 1 and tys % 100 != 11:
                parts.append(tys_slovo + " тысяча")
            elif tys % 10 in (2, 3, 4) and tys % 100 not in (12, 13, 14):
                parts.append(tys_slovo + " тысячи")
            else:
                parts.append(tys_slovo + " тысяч")
        if ostatok > 0:
            parts.append(under_thousand(ostatok))
        return " ".join(parts).strip()

    #разделяем строку
    g = str(x)
    for i in znak:
        if i in g:
            g = g.replace(i, '-' + i + '-')
    buk = [i.strip() for i in g.split('-')]
    buk=[x for x in buk if x]
    chisla = []  # сюда будем собирать числа и знаки
    for token in buk:  # buk — список токенов после split по знакам
        if token in znak:
            chisla.append(znak[token])
        else:
            words = token.split()  # разбиваем на отдельные слова
            if len(words) == 1:  # один элемент
                word = words[0]
                if word in word_to_num:
                    chisla.append(word_to_num[word])  # целое число
                elif word in znak:
                    chisla.append(znak[word])  # операция
            else:  # несколько слов, может быть число с дробной частью
                # разделяем по слову "и"
                parts = token.split(" и ")
                # целая часть
                val = 0
                for w in parts[0].split():
                    if w in word_to_num:
                        val += word_to_num[w]
                # дробная часть
                frac = 0
                if len(parts) > 1:
                    frac_words = parts[1].split()
                    frac_val = 0
                    multiplier = 0
                    for w in frac_words:
                        if w in word_to_num:
                            frac_val += word_to_num[w]
                        elif w in decimal_forms:
                            multiplier = decimal_forms[w]
                    frac = round(frac_val * multiplier, 3)
                number = val + frac
                chisla.append(number)
    chisla = eval(''.join(map(str, chisla)))
    def perrevod(chislas):
        cel = int(chislas)          # целая часть
        vivod = number_to_words(cel)  # словом или число как fallback
        drob = round(chislas - cel, 4)  # дробная часть
        print
        if drob != 0:
            vivod += " и"
            # переводим дробь в строку, убираем "0."
            drob_str = str(drob).split(".")[1]  
            length = len(drob_str)  # определяем разряд дроби
            drob_val = int(drob_str)
            # print(drob_val)
            vivod+=' '+number_to_words(drob_val)
            # переводим число дробной части в слова
            if drob_val==1:
                vivod += " одна"
                vivod += " " + decimal_forms.get(length, "")[:-2]+'ая'
            else:
                # vivod += " " + num_to_word.get(drob_val,'') 
                # добавляем слово разряда
                vivod += " " + decimal_forms.get(length, "")
        return vivod
    return(perrevod(chisla))
# тесты
# print('1)',calc("сорок пять и двадцать одна сотая разделить на семнадцать"))
# print('3)',calc("два плюс два умножить на два"))
# print('4)',calc("скобка открывается два плюс два скобка закрывается умножить скобка открывается четыре плюс четыре скобка закрывается"))
print('10',calc("два минус шисть"))