# def f(x):
#     a=''
#     while x>0:
#         a=str(x%3)+a
#         x=x//3
#     return a
# for n in range(1,15):
#     r=f(n)
#     if n%3==0:
#         r=r+r[-2:]
#     else:
#         r=r+str(f((n%3)*5))
#     r=int(r,3)
#     if r>=290:
#         print(n)
#         break
for n in range(3,100001):
    x='7'+'5'*n
    