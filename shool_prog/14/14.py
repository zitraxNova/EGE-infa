for x in range(3000, -1, -1):
    n = 7**100 - x
    k = 0
    while n:
        d = n % 7
        n = n // 7
        if d == 0:
            k += 1
    if k == 2:
        print(x)
        break
# 2989