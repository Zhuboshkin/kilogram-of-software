from itertools import*
from ipaddress import*
from string import*
from sys import*
from fnmatch import*

s='234 157 147 138 268 58 23 456'.split()
v='AF FH HC CB BD DG GA GF ED EB EH'.split()
print(*range(1,9))
for p in permutations('AFHCBDGE'):
    if all(str(p.index(a)+1) in s[p.index(b)] for a,b in v):
        print(*p)

def f(x,y,z,w):
    return not(((not x)or y)and (not w))or not(z and not(y and w))
for a in product([0,1],repeat=7):
    t=[(0,a[0],a[1],1),(a[2],1,a[3],a[4]),(1,0,a[5],a[6])]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(*p)

def f(x):
    n=x.count('1')+(x.count('2')*2)
    g=''
    while n>0:
        g=str(n%3)+g
        n=n//3
    return x+g
for x in range(1,1000000000):
    n=x
    g=''
    while n>0:
        g=str(n%3)+g
        n=n//3
    if x%3==0:
        g=g+g[-2::]
    else:
        g=f(g)
    g=int(g,3)
    if g>220 and g%2==0:
        print(g)
        break

cnt=0
for x in product('АВНРЬЯ',repeat=5):
    cnt+=1
    x=''.join(x)
    if x[0]!='Я' and x.count('Ь')<2 and x.count('ЯЯ')==0:
        print(cnt)
cnt=0
for l in open('1.txt'):
    arr=[int(x) for x in l.split()]
    arrp=[x for x in arr if arr.count(x)==3]
    arrpp=[x for x in arr if arr.count(x)>1]
    arrnp=[x for x in arr if arr.count(x)==1]
    if len(arrp)==6 and len(arrnp)==1:
        if sum(arrp)/len(arrpp) < sum(arrnp):
            cnt+=1
print(cnt)

for n in range(3,10000):
    x='1'+'2'*n
    while '12' in x or '322' in x or '222' in x:
        if '12' in x:
            x=x.replace('12','2',1)
        if '322' in x:
            x=x.replace('322','21',1)
        if '222' in x:
            x=x.replace('222','3',1)
    if x.count('1')+x.count('2')*2+x.count('3')*3==15:
        print(n)
        break

net=ip_network(f'218.194.82.148/255.255.255.192',0)
for ip in net:
    print(ip)

for x in printable[:25]:
    a=int('11353'+str(x)+'12',25)+int('135'+str(x)+'21',25)
    if a%24==0:
        print(a//24)

def f(x,y):
    return ((x-3*y)<a)or(y>400) or(x>56)
for a in range(10000):
    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
        print(a)

setrecursionlimit(10000)
def f(n):
    if n<5:return n
    if n>=5:return 2*n*f(n-4)
print((f(13766)-9*f(13762))/f(13758))

def f(x):
    if len(str(x))==5 and abs(x)%100==43:
        return 1
    else:
        return 0
arr=[int(x) for x in open('1.txt')]
cnt=0
ma=0
marr=max([x for x in arr if f(x)==1])
for i in range(2,len(arr)):
    if (f(arr[i-2]) +f(arr[i-1]) +f(arr[i]))>0:
        if arr[i-2]**2+arr[i-1]**2+arr[i]**2<marr**2:
            cnt+=1
            ma=max(ma,arr[i-2]**2+arr[i-1]**2+arr[i]**2)
print(cnt,ma)

def f(x,m):
    if x>131:return m%2==0
    if m==0:return 0
    h=[f(x+3,m-1),f(x+6,m-1),f(x*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(1,132) if f(s,2) and not f(s,1)])
print([s for s in range(1,132) if f(s,3) and not f(s,1)])
print([s for s in range(1,132) if f(s,4) and not f(s,2)])

def f(x,y):
    if x==y:return 1
    if x<y or x==24:return 0
    else:
        return f(x-1,y)+f(x-6,y)+f(x//2,y)
print(f(34,29)*f(29,19)*f(19,6))

arr=open('24_19254.txt').readline()
l=0
cnt=0
ma=0
for r in range(3,len(arr)):
    if arr[r-3]+arr[r-2]+arr[r-1]+arr[r]=='FSRQ':
        cnt+=1
    if cnt==80:
        ma=max(ma,r-l+1)
    while cnt>80:
        if arr[l]+arr[l+1]+arr[l+2]+arr[l+3]=='FSRQ':
            cnt-=1
        l+=1
print(ma)

for x in range(0,10**10,18579):
    if fnmatch(str(x),'54?1?3*7'):
        print(x,x//18579)

f=open('1.txt')
s=f.readline()
arr=[]
ma=[]
z=1
n=0
for l in f:
    a=[int(x) for x in l.split()]
    arr.append(a)
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


cla=[[],[]]
clb=[[],[],[]]
for l in open('a.txt'):
    x,y=[float(x) for x in l.split()]
    if y<8:
        cla[0].append([x,y])
    else:
        cla[1].append([x,y])
for l in open('b.txt'):
    x,y=[float(x) for x in l.split()]
    if y<8:
        clb[0].append([x,y])
    else:
        clb[1].append([x,y])
def d(A,B):
    x1,y1=A
    x2,y2=B
    return ((x2-x1)**2+(y2-y1)**2)**0.5
def centr(cl):
    m=[]
    for p in cl:
        ma=sum(d(p,p1) for p1 in cl)
        m.append([ma,p])
    return min(m)[1]
centra=[centr(cl) for cl in cla]
centrb=[centr(cl) for cl in clb]
pxa=sum(x for x,y in centra)/len(centra)*10000
pya=sum(y for x,y in centra)/len(centra)*10000
print(int(pxa),int(pya))