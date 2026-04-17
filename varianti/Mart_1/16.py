f = [0] * 15000
for n in range(15000):
    if n < 5:
        f[n] = n
    if n >= 5:
        f[n] = 2 * n * f[n - 4]

res = (f[13766] - 9 * f[13762]) // f[13758]
print(res)
# 757543052