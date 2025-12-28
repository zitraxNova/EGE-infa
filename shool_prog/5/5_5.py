for n in range(1, 100):
    bin_n = bin(n)[2:]
    bin_n = str(bin_n)
    if bin_n.count('1') > bin_n.count('0'):
        bin_n += '1'
    else:
        bin_n += '0'

    r = int(bin_n, 2)
    if r > 36:
        print(r)
        break
# 39