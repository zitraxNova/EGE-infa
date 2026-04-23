for n in range(1, 100):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'
    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '0'
    else:
        bin_n = bin_n + '1'

    r = int(bin_n, 2)
    if r > 253:
        print(n)
# 64

