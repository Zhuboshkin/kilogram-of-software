#минимальная длина
f=open('1.txt').readline()
l=0
g=[]
cnt=0
for i in range(2,len(f)):
    if f[i-2]+f[i-1]+f[i]=='RSQ':
        cnt+=1
    if cnt==130:
        g.append(i-l+1)
    while cnt==130:
        if f[l]+f[l+1]+f[l+2]=='RSQ':
            cnt-=1
            l+=1
        else:
            l+=1
print(min(g))
#Максимальная длина бкрем момент когда будет 131 а занчит 1 символ назд было 130
f=open('1.txt').readline()
l=0
r=0
g=[]
cnt=0
for i in range(2,len(f)):
    if f[i-2]+f[i-1]+f[i]=='RSQ':
        cnt+=1
    if cnt==131:
        r=i-1
        g.append(r-l+1)
    while cnt==131:
        if f[l]+f[l+1]+f[l+2]=='RSQ':
            cnt-=1
            l+=1
        else:
            l+=1
print(min(g))