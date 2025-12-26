from ipaddress import *

net = ip_network('192.124.96.0/255.255.240.0', 0)
k = 0
for ip in net:
    ip2 = bin(int(ip))[2:].zfill(32)
    if ip2[-1] == '0':
        k += 1
print(k)