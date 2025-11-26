max_x = 0
for x in range(1, 10000 + 1):
    n = 6**900 + 6**10 - x
    k_1 = 0
    k_2 = 0
    while n > 0:
        d = n % 6
        if d == 3:
            k_1 += 1
        if d == 5:
            k_2 += 1
        n = n // 6
    if k_1 == k_2:
        max_x = x
print(max_x)