for a in range(1, 1000):
        f = 1 # старт значение один, все хорошо
        for x in range(1, 1000):
                f *= (x & a == 0) or (x & 37 != 0) or (x & 12 != 0)
        if f == 1:
                print(a)
# 45
        
