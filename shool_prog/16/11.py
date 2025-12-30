def f(n):
    if n > 25:
        return n ** 2 + 2 * n + 1
    if n % 2 == 0 and n <= 25:
        return 2 * f(n + 1) + f(n + 3)
    if n % 2 != 0 and n <= 25:
        return f(n + 2) + 3 * f(n + 5)

k = 0
for n in range(1, 1001):
    if '0' not in str(f(n)):
        k += 1
print(k)
# 575