def num(n):
    d = []
    z = int(n ** 0.5)
    for i in range(2, z + 1):
        if n % i == 0:
            d.append(i)
            if n // i not in d: 
                d.append(n // i)
    return sorted(d)
#print(num(100))
#print(num(11))

n = 670000
k = 0
while k < 5:
    n += 1
    d = num(n)
    p = []
    for x in d:
        if len(num(x)) == 0:
            p.append(x)
    s = sum(p)
    if str(s)[-1] == '5':
        print(n , s)
        k += 1
            
            

