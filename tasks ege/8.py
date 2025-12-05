# product - повторяются
# permutations - не повторяются
from itertools import*

cnt=0
g='ИАЭ'
s='ДГШ'
for x in product('ДГИАШЭ',repeat=5):
    x=''.join(x)
    if x[0] not in g and x[-1] not in s:
        cnt+=1
print(cnt)

cnt=0
for x in product('АВНРЬЯ',repeat=5):
    cnt+=1
    x=''.join(x)
    if x[0]!='Я' and x.count('Ь')<2 and x.count('ЯЯ')==0:
        print(cnt)