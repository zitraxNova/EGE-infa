from ipaddress import *

net = ip_network('192.168.31.80/255.255.255.240', 0) # создает список допустимых ip адресов
max_s = 0
for ip in net:
        ip2 = bin(int(ip))[2:] # получаю двоичную строку или двоичный код ip адреса
        max_s = max(max_s, ip2.count('1'))
print(max_s)
