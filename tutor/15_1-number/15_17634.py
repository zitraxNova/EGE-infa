for a in range(0, 100):
        f = 1
        for x in range(1, 1000):
                for y in range(1, 1000):
                        f *= (x + y <= 30) or (y <= x + 2) or (y >= a)
                        if f == 0:
                                break
                if f == 0:
                        break
        if f == 1:
                print(a)
                
