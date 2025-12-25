from ipaddress import *

for mask in range(32):
    net = ip_network(f'115.12.69.38/{mask}', 0)
    if str(net.network_address) == '115.12.64.0':
        print(mask)

