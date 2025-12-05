from turtle import*
left(90)
for k in range (1,8):
    forward(10*40)
    right(120)
penup()    
for x in range (0,10):
    for y in range (-2,15):
        setpos(x*40,y*40)
        dot(4,"red")
forward(10)
backward(10)
left(10)
forward(10)
backward(10)
for x in range (1,5):
forward(10)
backward(10)
a=123
x=a[0:]
print(x)