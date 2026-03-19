for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and (y == (z <= w))
                if f == 1:
                    print(z, y, w, x, "|", f * 1)