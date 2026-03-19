for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 2 != 0:
        bin_n = bin_n.replace('1', '111')
    else:
        bin_n = bin_n.replace('0', '000')

    if int(bin_n, 2) > 701:
        print(n)
# 11
