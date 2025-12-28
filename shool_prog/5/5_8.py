
def R(n):
    bn = f'{n:b}'
    bn = bn + str(bn.count('1') % 2)
    bn = bn + str(bn.count('1') % 2)
    return int(bn, 2)

print(min(R(N) for N in range(1, 100) if R(N) > 75))

# 78