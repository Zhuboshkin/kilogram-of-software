# Одна куча
def f(s,m):
    if s>=54: return m%2==0
    if m==0: return 0
    h=[f(s+2,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print('19)',[s for s in range(1,53) if f(s,2)])
print('20)',[s for s in range(1,53) if f(s,3) and not f(s,1)])
print('21)',[s for s in range(1,53) if f(s,4) and  not f(s,2)])

# Две кучи
def f(a,b,m):
    if a+b>=45:return m%2==0
    if m==0: return 0
    h=[f(a+1,b,m-1),f(a*3,b,m-1),f(a,b+1,m-1),f(a,b*3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("19)5",[s for s in range(1,41) if f(4,s,2)])
print("20)",[s for s in range(1,41) if not f(4,s,1) and f(4,s,3)])
print("21)",[s for s in range(1,41) if not f(4,s,2) and f(4,s,4)])

# Три кучи
def f(a,b,c,m):
    if a+b+c>=71:return m%2==0
    if m==0:return 0
    h=[f(a+3,b,c,m-1),f(a*2,b,c,m-1),f(a,b+3,c,m-1),f(a,b*2,c,m-1),f(a,b,c+3,m-1),f(a,b,c*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print("19)15",[s for s in range(59) if f(7,5,s,2)])
print("20)14 58",[s for s in range(59) if not f(7,5,s,1) and f(7,5,s,3)])
print("21)",[s for s in range(59) if not f(7,5,s,2) and f(7,5,s,4)])


