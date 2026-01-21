for a in range(100, 0, -1):
    k = 1
    for x in range(0, 100):
        for y in range(0, 100):
            if not((2 * x + y != 110) or (x < y) or (a < x)):
                k = 0
    if k == 1:
        print(a)
        break