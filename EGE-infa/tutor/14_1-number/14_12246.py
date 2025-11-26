n = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
digits_9 = []
while n > 0:
    digits_9.append(n % 9)
    n = n // 9
k = sum(1 for d in digits_9 if d != 0)
print(k)
