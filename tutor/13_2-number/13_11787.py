from ipaddress import *

net = ip_network('101.157.240.0/255.255.252.0', 0)
k = 0
for ip in net:
        ip2 = bin(int(ip))[2:].zfill(32)
        left = ip2[:16]
        right = ip2[16:]
        if left.count('1') < right.count('1'):
                k += 1
print(k)
