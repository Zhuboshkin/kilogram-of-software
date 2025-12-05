cnt=0
for l in open('1.txt'):
    arr=[int(x) for x in l.split()]
    arrnp=[x for x in arr if arr.count(x)==1]
    arrp=[x for x in arr if arr.count(x)==3]
    if len(arrp)==6 and len(arrnp)==1:
        if max(set(arrp))>max(arrnp):
            cnt+=1
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