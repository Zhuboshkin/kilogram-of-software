# Перевод
# def f(x,y):
#     g=[]
#     while x>0:
#         g.append([x%y])
#         x=x//y
#     return g[::-1]

from string import*
for x in printable[:25]:
    a=int('11353'+str(x)+'12',25)+int('135'+str(x)+'21',25)
    if a%24==0:
        print(a//24)

for x in printable[:21]:
    a=int('82934'+str(x)+'2',21)+int('2924'+str(x)+str(x)+'7',21)+int('67564'+str(x)+'8',21)
    if a%20==0:
        print(a//20)
        break