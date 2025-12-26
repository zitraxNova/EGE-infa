from ipaddress import *
net1 = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for x in net1:
    net = ip_network(f'172.16.168.0/255.255.255.{x}', 0)
    f = 0
    for ip in net:
        ip2 = bin(int(ip))[2:].zfill(32)
        if ip2.count('0') % 7 == 0:
            f += 1
    if f == 35:
        print(x)
