def calc(x):
    # база чисел
    slovar_chisel = {
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
    chisla_v_slova = {
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
    operacii = {
        "плюс": "+",
        "минус": "-",
        "умножить": "*",
        "разделить": "/",
        "остаток": "%",
        "в степени": "**",
        'скобка открывается':'(',
        'скобка закрывается':')',
    }
    # словарь для преобразования дробных частей (разрядность -> форма слова)
    drobnye_formy = {
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
    
    def proverit_skobki(spisok_tokenov):
        schetchik = 0
        for token in spisok_tokenov:
            if token == '(': schetchik += 1
            if token == ')': schetchik -= 1
            if schetchik < 0: return False
        return schetchik == 0
    
    def proverit_delenie_na_nol(spisok_tokenov):
        for i in range(len(spisok_tokenov) - 1):
            if spisok_tokenov[i] == '/' and spisok_tokenov[i + 1] == 0:
                return False
        return True
    
    def chislo_v_slova(chislo):
        if chislo == 0:
            return "ноль"
        if chislo >= 1_000_000:
            return "один миллион" if chislo == 1_000_000 else "слишком большое число"

        def do_tysyachi(chislo_vnutri):
            if chislo_vnutri == 0:
                return ""
            if chislo_vnutri < 20:
                return chisla_v_slova.get(chislo_vnutri, "")
            if chislo_vnutri < 100:
                desyatki = (chislo_vnutri // 10) * 10
                edinicy = chislo_vnutri % 10
                if edinicy == 0:
                    return chisla_v_slova[desyatki]
                return chisla_v_slova[desyatki] + " " + chisla_v_slova[edinicy]
            # 100–999
            sotni = (chislo_vnutri // 100) * 100
            ostatok = chislo_vnutri % 100
            if ostatok == 0:
                return chisla_v_slova[sotni]
            return chisla_v_slova[sotni] + " " + do_tysyachi(ostatok)

        # Разбиваем число на тысячи и остаток
        tysyachi = chislo // 1000
        ostatok = chislo % 1000

        chasti = []
        if tysyachi > 0:
            slova_tysyach = do_tysyachi(tysyachi)
            # Склоняем "тысяча"
            if tysyachi % 10 == 1 and tysyachi % 100 != 11:
                chasti.append(slova_tysyach + " тысяча")
            elif tysyachi % 10 in (2, 3, 4) and tysyachi % 100 not in (12, 13, 14):
                chasti.append(slova_tysyach + " тысячи")
            else:
                chasti.append(slova_tysyach + " тысяч")
        if ostatok > 0:
            chasti.append(do_tysyachi(ostatok))
        return " ".join(chasti).strip()
    
    def preobrazovat_chislo(chislo_dlya_prevoda):
        celaya_chast = int(chislo_dlya_prevoda)
        resultat = chislo_v_slova(celaya_chast)
        drobnaya_chast = round(chislo_dlya_prevoda - celaya_chast, 4)
        
        if drobnaya_chast != 0:
            resultat += " и"
            # переводим дробь в строку, убираем "0."
            stroka_drobi = str(drobnaya_chast).split(".")[1]  
            razryad = len(stroka_drobi)
            znachenie_drobi = int(stroka_drobi)
            
            resultat += ' ' + chislo_v_slova(znachenie_drobi)
            
            if znachenie_drobi == 1:
                resultat += " одна"
                resultat += " " + drobnye_formy.get(razryad, "")[:-2] + 'ая'
            else:
                resultat += " " + drobnye_formy.get(razryad, "")
        return resultat

    #разделяем строку
    stroka_vvoda = str(x)
    for operaciya in operacii:
        if operaciya in stroka_vvoda:
            stroka_vvoda = stroka_vvoda.replace(operaciya, '-' + operaciya + '-')
    
    tokeny = [token.strip() for token in stroka_vvoda.split('-')]
    tokeny = [token for token in tokeny if token]
    
    spisok_chisel = []  # сюда будем собирать числа и знаки
    for token in tokeny:
        if token in operacii:
            spisok_chisel.append(operacii[token])
        else:
            slova = token.split()
            if len(slova) == 1:
                slovo = slova[0]
                if slovo in slovar_chisel:
                    spisok_chisel.append(slovar_chisel[slovo])
                else:
                    return 'Неправильная запись числа {' + str(slovo) + '}'
            else:
                # разделяем по слову "и"
                chasti = token.split(" и ")
                # целая часть
                znachenie = 0
                for slovo in chasti[0].split():
                    if slovo in slovar_chisel:
                        znachenie += slovar_chisel[slovo]
                # дробная часть
                drob = 0
                if len(chasti) > 1:
                    slova_drobi = chasti[1].split()
                    znachenie_drobi = 0
                    mnozhitel = 0
                    for slovo in slova_drobi:
                        if slovo in slovar_chisel:
                            znachenie_drobi += slovar_chisel[slovo]
                        elif slovo in drobnye_formy:
                            mnozhitel = drobnye_formy[slovo]
                    drob = round(znachenie_drobi * mnozhitel, 3)
                chislo = znachenie + drob
                spisok_chisel.append(chislo)
    
    if str(spisok_chisel[0]) in '+-*/%**' or str(spisok_chisel[-1]) in '+-*/%**':
        return 'Неправильную последовательность чисел или операций'
    elif not proverit_delenie_na_nol(spisok_chisel):
        return 'Деление на ноль'
    elif not proverit_skobki(spisok_chisel):
        return 'Несбалансированные скобки'
    else:
        resultat_vichisleniya = eval(''.join(map(str, spisok_chisel)))
        return preobrazovat_chislo(resultat_vichisleniya)

# тесты
print('1)', calc("сорок пять и двадцать одна сотая разделить на семнадцать"))
print('3)', calc("два плюс два умножить на два"))
print('4)', calc("скобка открывается два плюс два скобка закрывается умножить скобка открывается четыре плюс четыре скобка закрывается"))
print('Ошибки')
# 1)неправильную запись числа; два плюс шисть
print('1)', calc('два плюс шисть'))
# 2)неправильную последовательность чисел или операций
print('2)', calc('два два минус')) 
print('2)', calc('минус два два'))
# 3)деление на ноль; пять разделить на ноль
print('3)', calc('пять разделить на ноль'))
# 4)Несбалансированные скобки; скобка два умножить на два плюс два
print('4)', calc('скобка открывается два умножить на два плюс два'))