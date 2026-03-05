def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d:
                d.append(n // i)
    return sorted(d)

k = 0
x = 200000000
while k < 5:
    d = num(x)
    if len(d) >= 5:
        s = d[0] * d[1] * d[2] * d[3] * d[4]
        if s % 10 == 1 and s <= x:
            print(s, d[4])
            k += 1
    x += 1
