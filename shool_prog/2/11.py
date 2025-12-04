for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x == (not y)) <= ((x and w) == z)
                if f == 0:
                    print(y, z, x, w, '|', f * 1)
# yzxw