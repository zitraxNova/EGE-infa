from ipaddress import *

k = 0
net = ip_network('112.208.0.0/255.255.224.0')
for ip in net:
    ip2 = bin(int(ip))[2:]
    if ip2[-3] == ip2[-2] == ip2[-1]:
        k += 1
print(k)