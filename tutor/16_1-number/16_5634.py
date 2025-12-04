f = [0] * 6000

for n in range(1, 6000):
    if n == 1:
        f[n] = 1
    else:
        f[n] = f[n - 1] + n * f[n - 1]
print(f[5997] // f[5995])
# 35970006