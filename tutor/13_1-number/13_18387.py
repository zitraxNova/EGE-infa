from ipaddress import *
for a in range(256):
        net = ip_network(f'192.214.{a}.184/255.255.255.224', 0)
        f = 1
        for ip in net:
                ip2 = bin(int(ip))[2:]
                if ip2.count('1') > 15:
                        f = 1
                else:
                        f = 0
                        break
        if f == 1:
                print(a)
