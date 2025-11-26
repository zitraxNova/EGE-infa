n = 4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3
k = 0
while n > 0:
        d = n % 4
        if d == 3:
                k += 1
        n = n // 4
print(k)