def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(1, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d:
                d.append(n // i)
    return sorted(d)


# print(num(100))
# print(num(11))

n = 6086055
k = 0
while k < 10:
    n += 1
    d = num(n)
    p = []
    for x in d:
        if len(num(x)) == 2:
            p.append(x)
    if len(p) > 0:
        for x in p:
            for y in p:
                if x * y == n and str(x).count('6') == 1 and str(y).count('6') == 1:
                    print(n, max(x, y))
                    k += 1


