def Del(n, m):
    return n % m == 0


for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        if Del(405, x) and not Del(81, x) and a - x <= 162:
            f = 0
            break
    if f == 1:
        print(a)
        break
