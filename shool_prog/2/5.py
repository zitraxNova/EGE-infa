for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x or ((not y) or z or w) and (y or (not w))
                if f == 0:
                    print(y, w, z, x, '|', f * 1)
                    
# ywzx
