def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(1, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)


for x in range(154026, 154043):
    d = num(x)
    if len(d) == 4:
        print(d[2], d[3])