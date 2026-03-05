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
for i in range(800_001,1_000_000):
    if num(i):
        print(i,num(i))
        k += 1
    if k == 5:
        break

