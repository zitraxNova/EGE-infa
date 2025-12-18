for a in range(0, 100):
        f = 1
        for x in range(0, 1000):
                for y in range(0, 1000):
                        f *= (2 * x + y != 110) or (x < y) or (a < x)
                        if f == 0:
                                break
                if f == 0:
                        break
        if f == 1:
                print(a)
                
