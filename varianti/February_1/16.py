f = [0] * 50000
for n in range(1, 50000):
    if n < 20:
        f[n] = n
    if n >= 20:
        f[n] = (n - 6) * f[n - 7]

res = (f[47872] - 290 * f[47865]) // f[47858]
print(res)
# 2276939784