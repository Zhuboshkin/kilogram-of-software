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


for x in range(3,10000):
    a='3'+'1'*x
    while '31' in a or '211' in a or '1111' in a:
        if '31' in a:
            a=a.replace('31','1',1)
        if '211' in a:
            a=a.replace('211','13',1)
        if '1111' in a:
            a=a.replace('1111','2',1)
    if a.count('1')+a.count('2')*2+a.count('3')*3==15:
        print(x)