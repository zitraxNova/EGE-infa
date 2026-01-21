f = [0] * 2500
for n in range(2500):
    if n >= 2025:
        f[n] = n
    if n < 2025:
        f[n] = n * 2 + f[n + 2]
res = f[82] - f[81]
print(res)
# 2


def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + f(n + 2)
    
print(f(82) - f(81))