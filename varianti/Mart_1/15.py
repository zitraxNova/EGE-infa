for a in range(0, 100):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            f *= (x - 3 * y < a) or (y > 400) or (x > 56)
            if f == 0:
                break
        if f == 0:
            break
    if f == 1:
        print(a)
# 54