#Билеты в кинотеатр
f = open('1.txt')
N, M, K = [int(x) for x in f.readline().split()]
seats = ['0'] * (K+1)
trow=0
g = []
cnt=0
for line in f:
    row, seat = [int(x) for x in line.split()]
    g.append([row,seat])
g = sorted(g)
tseats=''.join(seats)
while '00' in tseats:
    throw = g[cnt][0]
    seats[g[cnt][1]]='1'
    tseats = ''.join(seats)
    if "00" in tseats:
        ssr = tseats
    cnt+=1
print(throw-1,ssr.find("00"))

#Елки
f=open('1.txt')
g=[]
for l in f:
    row,seat=[int(x) for x in l.split()]
    g.append([row,seat])
g=sorted(g,reverse=1)
k=0
j=1
h=[]
for j in range(len(g)):
    if g[j-1][0]==g[j][0] and g[j-1][1]-g[j][1]==14:
        print(g[j-1][0],g[j][1]+1)
        break

#Экзамен
f = open('1.txt')
g = []
arr = []
cnt = [int(x) for x in f.readline().split()]
cnt = int(cnt[0] * 0.25) - 1
k = 0
for l in f:
    ex = [int(x) for x in l.split()]
    if ex.count(2) == 0:
        g.append([(ex[1] + ex[2] + ex[3] + ex[4]) / 4, ex[0]])
    if ex.count(2) > 2:
        arr.append([(ex[1] + ex[2] + ex[3] + ex[4]) / 4, ex[0]])
g = sorted(g, key=lambda x: (-x[0], x[1]))
arr = sorted(arr, key=lambda x: (-x[0], x[1]))
print(g[cnt][1], arr[0][1])

#Коробки
g=[]
arr=sorted([int(x) for x in open('1.txt')],reverse=1)
for i in range(len(arr)):
    k=1
    for j in range(i,len(arr)):
        if arr[i]-arr[j]>=9:
            k+=1
            i=j
    g.append([k,arr[j]])
print(g)

#Задачки
f=open('1.txt')
s=f.readline()
arr=[]
ma=[]
z=1
n=0
for l in f:
    a=[int(x) for x in l.split()]
    arr.append(a)
    arr
arr=sorted(arr,key=lambda x:(x[0],-x[1]))
for i in range(len(arr)-1):
    if arr[i][0]==arr[i+1][0]:
        n=arr[i][0]
        if arr[i][1]-arr[i+1][1]==1:
            z=z+1
        if arr[i][1]==arr[i+1][1]:
            z=z+0
        if arr[i][1]-arr[i+1][1]>1:
            z=1
    else:
        ma.append([z,n])
        z=1
        n=0
ma=sorted(ma,key=lambda x:(-x[0],x[1]))
print(ma[0][1],ma[0][0])