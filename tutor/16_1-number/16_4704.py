f = [0]*2500
for n in range(1, 2500):
        if n == 1:
                f[n] = 1
        else:
                f[n] = n * f[n-1]
print(f[2023]//f[2020])

# 8266912626