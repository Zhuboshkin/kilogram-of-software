#Делители
k=0
def f(x):
    g=[]
    for i in range(2,int(x*0.5)+1):
        if x%i==0:
            g.append(i)
            g.append(x//i)
    return sorted(set(g))
for t in range(1125000,10000000):
    arr=[x for x in f(t) if x%10==7 and x!=7 and x!=t]
    if len(arr)>0:
        print(t,arr[0])
        k+=1
    if k==5:
        break


# #Проверка на маску
from fnmatch import*
for x in range(0,10**10,18579):
    if fnmatch(str(x),'54?1?3*7'):
        print(x,x//18579)