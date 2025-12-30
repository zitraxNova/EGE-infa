f = [0] * 1500
for n in range(1500):
    if n < 3:
        f[n] = 1
    if n > 2:
        f[n] = f[n - 1] + f[n - 2]

res = (f[1006] - f[1004]) // f[1005]
print(res)

# 1