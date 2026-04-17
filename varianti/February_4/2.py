for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = w and ((not x) or y) and ((not y) and z or y and (not z))
                if f == 1:
                    print(y, x, z, w, '|', f * 1)
# yxzw
