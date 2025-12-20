for a in range(0,100):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            f *= (11 <= y) or (7 * y < x) or (a > x * y)
            if f == 0:
                break
        if f == 0:
            break
    if f == 1:
        print(a)