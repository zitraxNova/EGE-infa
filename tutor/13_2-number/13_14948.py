from ipaddress import *

net = ip_network('192.168.32.128/255.255.255.192', 0)
k = 0
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2.count('1') % 2 == 0:
        k += 1
print(k) 