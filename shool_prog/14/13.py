for x in range(2030, 0, -1):
    n = 7**170 + 7**100 - x
    k = 0
    while n:
        if n % 7 == 0:
            k += 1
        n = n // 7
    if k == 70:
        print(x)
        break
# 2001