f = [0] * 2500
for n in range(2500):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = 2 * n * f[n-1]


a = (f[2024] // 16 - f[2023]) // f[2022]
print(a)

# 1019592