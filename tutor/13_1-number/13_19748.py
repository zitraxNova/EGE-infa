"""
ip1 157.220.185.237
ip2 157.220.185.230
m   255.255. x . 0
as  157.220.   . 0
"""


from ipaddress import *
m = [0,128,192,224,240,248,252,254,255]
for x in m:
        if 185 & x == 184 & x:
                print(x)
m = [0,128,192,224,240,248,252,254]
for a in m:
        net = ip_network(f'157.220.185.237/255.255.{a}.0', 0)
        k15 = 0
        for ip in net:
                ip2 = bin(int(ip))[2:]
                if ip2.count('1') == 15:
                        k15 += 1
        print(a, k15)
                        
                
