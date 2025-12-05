#Игра 1
import random
def g(x):
    pro=0
    for i in x:
        if i not in '0123456789':
            pro=1
    return pro
def f(x):
    x=str(x)
    flag=0
    for i in x:
        if x.count(i)>1:
            flag=1
    return flag
igra=1
def game(za,ot):
    if za==ot:
        print('япии ты отгадал')
    else:
        kor=0
        buk=0
        for i in range(4):
            if ot[i] in za:
                if za[i] == ot[i]:
                    buk += 1
                else:
                    kor += 1
        print('Коров:',kor,'Быков:',buk)
zagad='0'
while zagad[0]=='0':
    zagad = "".join(random.sample("0123456789",4))
korect=0
while igra==1:
    while korect==0:
        print('Напишите 4-значное число с неповторяющимися цифрами')
        otgad=str(input())
        if len(otgad)!=4:
            print('Число должно быть 4-значным')
        elif otgad[0]=='0':
            print('Число не должно начинаться с 0')
        elif  f(otgad)==1:
            print('Цифры не должны повторяться')
        elif g(otgad)==1:
            print('Все символы должны быть цифрами')
        elif len(otgad)==4 and otgad[0]!='0' and f(otgad)==0 and f(otgad)==0:
            korect=1
    korect=0
    if zagad == otgad:
        print('япии ты отгадал')
        igra=0
    else:
        game(zagad,otgad)
    