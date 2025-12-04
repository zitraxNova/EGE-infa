f = [0] * 2500
for n in range(2500):
        if n < 4:
                f[n] = 1
        if n > 3 and n % 2 != 0:
            f[n] = n
        else:
                f[n] = f[n-1] + f[n-2] + f[n-3]
a = f[2254] - f[2252]
print(a)

# 4504