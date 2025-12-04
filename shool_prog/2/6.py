for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) <= (y == z)
            if f == 0:
                print(y, x, z, '|', f * 1)
# yxz
