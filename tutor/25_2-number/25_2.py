def num(n):
    d = set()  
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(list(d))

k = 0
x = 200000001
while k < 5:
    d = num(x)
    if len(d) >= 5:
        d = d[:5]  
        s = 1
        for i in d:
            s *= i
        if 0 < s < x:
            print(s)
            k += 1
    
    x += 1