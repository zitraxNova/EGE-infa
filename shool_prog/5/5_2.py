def R(N):
    bn = f'{N:b}'[1:]
    if bn.count('1') % 2 == 0:
        bn = '10' + bn
    else:
        bn = '1' + bn + '0'
    return int(bn, 2)


print(max(R(N) for N in range(2, 450) if R(N) < 450))