from ipaddress import IPv4Network


network = IPv4Network("112.208.0.0/19")
count = 0
for addr in network.hosts():
    last_byte = int(addr) & 0xFF  
    if (last_byte & 0b111 == 0b000) or (last_byte & 0b111 == 0b111):
        count += 1


print(count)