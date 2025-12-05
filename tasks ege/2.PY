print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=not(x<=z)or(y==w)or y
                if f==0:
                    print(x,y,z,w)

from itertools import*
def f(x,y,z,w):
    return not(x<=z)or(y==w)or y
for a in product([0,1],repeat=7):
    table=[(1,0,a[0],a[1]),(a[2],1,0,a[3]),(0,a[4],a[5],a[6])]
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
                print(p)
