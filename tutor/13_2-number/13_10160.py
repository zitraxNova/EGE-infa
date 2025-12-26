from ipaddress import *

for mask in range(32):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    if str(net.network_address) == '76.155.48.0':
        print(mask)