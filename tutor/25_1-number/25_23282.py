def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d:
                d.append(n // i)
    return sorted(d)


# print(num(100))
# print(num(11))

n = 5400000
k = 0
while k < 5:
    n += 1
    d = num(n)
    p = []
    for x in d:
        if len(num(x)) == 0:
            p.append(x)
    if len(p) > 0:
        m = min(p) + max(p)
        if m > 60000 and str(m) == str(m)[::-1]:
            print(n, m)
            k += 1
            
    


