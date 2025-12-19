def Del(n, m):
        return n % m == 0
for a in range(1, 1000):
        f = 1
        for x in range(1, 1000):
                #f *= not(Del(x, 128)) or (Del(x, a)) or not (Del(x, 80))
                f *= Del(x, 128) == 0 or Del(x, a) == 1 or Del(x, 80) == 0
                f *= (x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))
        if f == 1:
                print(a)
