def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(1, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)


k = 0
for x in range(500001, 501000):
    d = num(x)
    if sum(d) % 10 == 6:
        print(x, sum(d))
        k += 1
        if k == 5:
            break
   

