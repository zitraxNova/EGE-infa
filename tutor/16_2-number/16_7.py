f = [0] * 2500
for n in range(2500):
    if n == 1:
        f[n] = 2025
    if n > 1:
        f[n] = 3 * (n - 1) * f[n - 2]


a = f[2027] // f[2023]
print(a)

# 36905616