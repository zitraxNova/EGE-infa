for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == z) and (not(y <= w)) and (not x)
                if f == 0:
                    print(y, z, x, w, '|', f * 1 )