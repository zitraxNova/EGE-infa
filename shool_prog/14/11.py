k = 0
for x in range(6, 80):
    n1 = 5 * x**4 + 5 * x**3 + 1 * x**2 + 1 * x + 3
    n2 = 7 * 80**3 + x * 80**2 + x * 80 + 5
    k += int(abs(n1 - n2) <= 1_000_000)
print(k)
# 4