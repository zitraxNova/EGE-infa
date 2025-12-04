def f(n):
    return 2 * (g[n - 3] + 8)
g = [0] * 16000
for n in range(16000):
    if n < 10:
        g[n] = 2 * n
    else:
        g[n] = g[n - 2] + 1
    print(2 * (g[15548 - 3] + 8))
    print(f(15548))
# 15588