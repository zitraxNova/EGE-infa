for x in range(1, 5555+1):
        n = 5 ** 150 + 5 ** 135 - x
        k = 0
        while n > 0:
                d = n % 5
                if d == 4:
                        k += 1
                n = n // 5
        if k == 134:
                print(x)
                
# 3126