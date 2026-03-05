def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)



for x in range(700001, 701000):
    d = [i for i in num(x) if i % 10 == 7]
    if len(d) > 0:
        print(x, min(d))
    

