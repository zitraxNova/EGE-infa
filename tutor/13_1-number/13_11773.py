from ipaddress import *

net = ip_network('87.226.26.72/255.255.255.252', 0)
k = 0
for ip in net:
        ip2 = bin(int(ip))[2:].zfill(32)#достраиваю двоичную строку до указанного разряда по необходимости
        if ip2.count('0') % 2 == 0:
                k += 1
print(k)



# 2 вариант
from ipaddress import *

net = ip_network('87.226.26.72/255.255.255.252', 0)
k = 0
for ip in net:
        ip2 = bin(int(ip))[2:]
        k0 = 32 - ip2.count('1')
        if k0 % 2 == 0:
                k += 1
print(k)
