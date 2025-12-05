for n in range(1000):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    r=int(r,2)
    if r>480:
        print(n)
        break
    
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