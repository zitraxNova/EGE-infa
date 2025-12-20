for a in range(1, 10000):
    if all(((x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0))) == 1 for x in range(1, 10000)):
        print(a)
