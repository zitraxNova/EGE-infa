from ipaddress import *

net = ip_network('112.208.0.0/255.255.128.0', 0)
k = 0
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2.count('1') % 11 != 0:
        k += 1
print(k)


