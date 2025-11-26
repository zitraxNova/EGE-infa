for x in range(1, 2030 + 1):
    n = 6**260 + 6**160 + 6**60 - x
    k = 0
    while n > 0:
        if n % 6 == 0:
            k += 1
        n = n // 6
    if k == 202:
        print(x)
