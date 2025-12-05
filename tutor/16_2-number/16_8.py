def f(n):
    return g[n-1] + g[n-3]
g = [0] * 50000
for n in range(50000):
    if n <= 9:
        g[n] = 3 * n
    if n > 9:
        g[n] = g[n-4] + 2


print(g[n-1])
print(f(42999))

# 43032