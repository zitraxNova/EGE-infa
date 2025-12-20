for a in range(-1000, 1000):
    f = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x > 68) or (y > 89) or (2 * x - 7 * y < a)):
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(a)
        break