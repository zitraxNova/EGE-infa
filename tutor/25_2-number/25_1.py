def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(1, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)


n = 800000
k = 0
while k < 5:
    n += 1
    d = num(n)
    if len(d) > 2:
        mn = d[1]
        mx = d[-2]
        s = mn + mx
        if s % 138 == 0:
            print(n, s)
            k += 1
            
