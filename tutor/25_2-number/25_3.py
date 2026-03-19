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
n = 10000000
while k < 5:
    n += 1
    d = num(n)
    if len(d) < 2:
        s = d[-1] + d[-2] + d[-3]
        z = int(s ** 0.5)
        if z ** 2 == s:
            print(s)