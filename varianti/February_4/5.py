m = []
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if bin_n.count('0') % 2 == 0:
        bin_n = '1' + bin_n + '1'
    else:
        bin_n = '10' + bin_n
    r = int(bin_n, 2)
    if r < 100:
        m.append(r)
print(max(m)) 
# 97