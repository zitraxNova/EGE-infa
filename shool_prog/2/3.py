for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x <= y) and (y <= z)
            if f == 1:
                print(z, x, y, '|', f * 1)
# zxy

