for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a <= b) <= ((not a) and c)
            if f == 1:
                print(a, c, b, '|', f * 1)
# acb