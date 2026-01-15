max_R = 0
for n in range(1, 13):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_r = '10' + bin_n
    else:
        bin_r = '1' + bin_n + '01'

    R = int(bin_r, 2)
    max_R = max(max_R, R)
    print(max_R)
# 109