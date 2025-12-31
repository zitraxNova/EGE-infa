def R(N):
    bn = f'{N:b}'
    bn += bn[-2]
    bn += bn[1]
    return int(bn, 2)


for N in range(2, 1000):
    if R(N) > 170:
        print(N)
        break

# 43