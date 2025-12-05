#поле
bord={"a1": " ", "a2": " ", "a3": " ",
    "b1": " ", "b2": " ", "b3": " ",
    "c1": " ", "c2": " ", "c3": " "}
#функция создания поля
def printpole(board):
    pole = (f"a {board['a1']} | {board['a2']} | {board['a3']}\n"
            f"b {board['b1']} | {board['b2']} | {board['b3']}\n"
            f"c {board['c1']} | {board['c2']} | {board['c3']}\n")
    print('  1   2   3')
    print(pole)
    
printpole(bord)
game=1
XiO='X'
#начало игры
while game==1:
    print(f'Игрок {XiO}, введите координаты строки и столбца через пробел (например: a 1):')
    g=input().split()
    #проверка на коррекнтость
    if len(g)!=2 or g[0] not in 'abc' or g[1] not in '123':
        print('Некорректный ввод. Введите букву и число через пробел.')
        continue
    hod=g[0]+g[1]
    if bord[hod]!=' ':
        print("Эта клетка уже занята. Выберете другую клутку.")
        continue
    else:
        bord[hod]=XiO
        printpole(bord)
    #случий ничьи
    if all(bord[cell] != ' ' for cell in bord):
        print("Ничья. Конец игры")
        game = 0
    #случии победы
    elif bord['a1']==bord['a2']==bord['a3'] and bord['a1']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['b1']==bord['b2']==bord['b3'] and bord['b1']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['c1']==bord['c2']==bord['c3'] and bord['c1']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['a1']==bord['b1']==bord['c1'] and bord['a1']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['a2']==bord['b2']==bord['c2'] and bord['a2']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['a3']==bord['b3']==bord['c3'] and bord['a3']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['a1']==bord['b2']==bord['c3'] and bord['a1']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    elif bord['a3']==bord['b2']==bord['c1'] and bord['a3']!=' ':
        print(f'ЯПИИИИИИИИИ!!!!! Победил игрок {XiO}. Конец игры')
        game=0
    #перемена хода
    XiO = "O" if XiO == "X" else "X"
    