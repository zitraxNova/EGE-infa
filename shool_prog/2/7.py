for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((not x) or (not z)) <= (x == y)
            if f == 0:
                print(z, x, y, '|', f * 1)
# zxy