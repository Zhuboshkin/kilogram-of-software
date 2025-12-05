# Уменьшаем
def f(x,y):
    if x==y:return 1
    if x<y or x==24:return 0
    else:
        return f(x-1,y)+f(x-6,y)+f(x//2,y)
print(f(34,29)*f(29,19)*f(19,6))


# Увеличиваем
def f(x,y):
    if x==y:return 1
    if x>y or x==35:return 0
    else:
        return f(x+1,y)+f(x+2,y)+f(x*2,y)
print(f(7,13)*f(13,15)*f(15,51))