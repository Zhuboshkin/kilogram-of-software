from ipaddress import*
#Есть сеть и ip что-то с маской
for mask in range(33):
    net=ip_network(f'173.103.25.118/{mask}',0)
    print(net,32-mask)

# Есть только маска и надо найти кол адресов
net=ip_network(f'0.0.0.0/255.255.240.0',0)
print(net.num_addresses-2)

# 2 ip адресса и найти маску
for mask in range(33):
    net1=ip_network(f'165.112.200.70/{mask}',0)
    net2=ip_network(f'165.112.175.80/{mask}',0)
    if net1==net2:
        print(mask)   

#  Задача на деление на x
from ipaddress import *
cnt=0
net=ip_network(f'123.222.111.192/255.255.255.248',0)
for ip in net:
    ip_2=bin(int(ip))[2:].zfill(32)
    if ip_2.count("0")%3!=0:
        cnt+=1
print(cnt)

# Нахождение минимального значения
from ipaddress import *
for mask in range(33):
    net=ip_network(f'204.108.112.142/{mask}',0)
    print(net,32-mask)

# Нахождение ip
net=ip_network(f'192.168.240.0/255.255.255.0',0)
for ip in net:
    ip1=bin(int(ip))[2:].zfill(32)
    if ip1.count('1')==ip1.count('0'):
        print(ip1)

# Наибольший ip берем предпоследний
net=ip_network(f'143.168.72.213/255.255.255.240',0)
for ip in net:
    print(ip)