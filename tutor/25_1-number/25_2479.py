def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d:
                d.append(n // i)
    return sorted(d)

for x in range(4000001, 4000200):
    d = num(x)
    if len(d) >= 5:
        s = d[-5] + d[-4] + d[-3] + d[-2] + d[-1]
        if s % 10 == 0:
            print(x, s)
