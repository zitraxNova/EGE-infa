for a in range(0, 100):
        f = 1
        for x in range(1, 1000):
                for y in range(1, 1000):
                        f *= (x < a) or (y < 3 * a) or (2 * x + y > 128)
                        if f == 0:
                                break
                if f == 0:
                        break
        if f == 1:
                print(a)
                
