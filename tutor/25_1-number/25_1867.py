def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(1, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)
#print(num(100))
#print(num(11))

n = 500000
k = 0
while k < 5:
    n += 1
    d = num(n)
    d_8 = []
    for x in d:
        if x % 10 == 8 and x != 8 and x != n:
            d_8.append(x)
    if len(d_8) > 0:
        print(n, min(d_8)) # d8[0]
        k += 1
