for a in range(0, 1000):
    f = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (y <= 5) and (x <= 32) and (x + 2 * y >= a):
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(a)
        break
