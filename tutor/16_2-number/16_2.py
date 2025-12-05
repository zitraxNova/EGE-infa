f = [0] * 2500
for n in range(2500):
    if n <= 4:
        f[n] = 1
    if n > 5:
        f[n] = n + f[n-2]
print(f[2126] - f[2122])

# 4250