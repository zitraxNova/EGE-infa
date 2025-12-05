f = [0] * 2500
for n in range(2500):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n-1]


a = (f[2024] // 4 + f[2023]) // f[2022]
print(a)

# 1025661