G = {}
F = {}

for n in range(248100, 0, -1):
    if n >= 248045:
        G[n] = n / 20 + 28
    else:
        G[n] = G[n + 9] - 4
for n in range(8, 700):
    if n < 19:
        F[n] = 6 * (G[n-7] - 36)
    else:
        F[n] = F[n-4] + 3580
print(F[673])