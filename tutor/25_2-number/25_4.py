def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)


n = 220000
k = 0
while k < 5:
    n += 1
    d = num(n)
    if len(d) > 0:
        m = min(d) + max(d)
        if m % 10 == 4: 
            print(n, m)
            k += 1
