#Обычная задача
def f(x,y):
    return (5<y)or(x>32)or(x+2*y<a)
for a in range(1000):
    if all(f(x,y)==1 for x in range(1000) for y in range(1000)):
        print(a)


def f(x, a1, a2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not (C or J)) <= (not A)
g = []
# Теперь проверяем всю прямую, а не только границы
for a1 in range(0, 150):
    for a2 in range(a1, 150):
        if all(f(x, a1, a2) for x in range(0,150)):
            g.append(a2 - a1)

print(max(g))