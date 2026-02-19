def count_zero(num):
    count = 0
    while num:
        if num % 4 == 0:
            count += 1
        num //= 4
    return count


max_zeros = 0

for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    max_zeros = max(max_zeros, count_zero(num))


for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    if count_zero(num) == max_zeros:
        print(x)
        break