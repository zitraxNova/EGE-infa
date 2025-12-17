for x in range(1, 27000 + 1):
    n = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    k = 0
    while n > 0:
        if n % 27 == 0:
            k += 1
        n = n // 27
    if k == 6:
        print(x)
        break 

