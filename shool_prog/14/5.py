n = 17 ** 5 + 85 ** 8 - 10
k = 0
while n > 0:
    if n % 17 == 16:
        k += 1
    n = n // 17
print(k)
# 5