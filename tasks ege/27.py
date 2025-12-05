#Класторы
cla=[[],[]]
clb=[[],[],[]]
for l in open('A.txt'):
    x,y=[float(x) for x in l.split()]
    if y<3:
        cla[0].append([x,y])
    else:
        cla[1].append([x,y])
for l in open('B.txt'):
    x,y=[float(x) for x in l.split()]
    if y<3:
        clb[0].append([x,y])
    elif x>5:
        clb[1].append([x,y])
    else:
        clb[2].append([x,y])
def f(A,B):
    x1,y1=A
    x2,y2=B
    return ((x2 - x1)**2+(y2 - y1)**2)**0.5
def centr(cl):
    m=[]
    for p in cl:
        sm=sum(f(p,p1)for p1 in cl)
        m.append([sm,p])
    return min(m)[1]
centrA=[centr(cl) for cl in cla]
centrB=[centr(cl) for cl in clb]
pxa=sum(x for x, y in centrA)/len(centrA)*10000
pya=sum(y for x, y in centrA)/len(centrA)*10000
pxb=sum(x for x, y in centrB)/len(centrA)*10000
pyb=sum(y for x, y in centrB)/len(centrA)*10000
print(int(pxa),int(pya))
print(int(pxb),int(pyb))

toch=[]
for l in open('b.txt'):
    x,y=[float(x) for x in l.split()]
    toch.append([x,y])
from math import*
clasters=[]
while toch:
    cl=[toch.pop()]
    for p in cl:
        sosed=[x for x in toch if dist(x,p)<2]
        for p1 in sosed:
            toch.remove(p1)
            cl.append(p1)
    clasters.append(cl)
def centr(cl):
    m=[]
    for p in cl:
        mu=sum(dist(p,p1) for p1 in cl)
        m.append([mu,p])
    return min(m)[1]
centro=[centr(x) for x in clasters]
pxa=sum(x for x,y in centro)/len(centro)*10000
pya=sum(y for x,y in centro)/len(centro)*10000
print(pxa,pya)


#Дыры
def dist(p1, p2):
    return ((p1[0] - p2[0]) **2 + (p1[1] - p2[1]) ** 2) ** 0.5
f = open('1.txt')
n = int(f.readline())
blacks = []
ans = []
for i in range(n):
    blacks.append(list(map(float, f.readline().split())))
stars = []
for s in f:
    stars.append(list(map(float, s.split())))
for b in blacks:
    distances = []
    for s in stars:
        d = dist(b, s)
        if b[2] <= d <= 3 * b[2]:
            distances.append(d - b[2])
    if distances:  # Проверка, что distances не пуст
        sr_ar = sum(distances) / len(distances)
        ans.append(int(sr_ar * 1000))
print(max(ans), min(ans))

