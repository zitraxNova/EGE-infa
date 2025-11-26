for x in range(100000):
    n = 3 ** 2000 + 30 ** 10 - x
    k = 0
    while n != 0:
        d = n % 3
        if d == 2:
            k += 1
        n = n // 3
    if k == 2000:
        print(x)

# ?