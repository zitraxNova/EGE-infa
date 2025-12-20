for a in range(0, 1000):
    f = 1
    for x in range(1, 300):
        if f == 0:
            break
        for y in range(1, 300):
            func = (x - y >= 39) or (y <= x) or (y >= a - 20)
            if func == 0:
                f = 0
                break
    if f == 1:
        print(a)
