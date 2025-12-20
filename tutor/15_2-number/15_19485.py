def g(x):
    b = 170 <= x <= 220
    return (x % a == 0) or (b <= (x % 24 != 0))


f = 0
for a in range(1, 1000):
    if all(g(x) == 1 for x in range(1, 1000000)):
        f += 1
print(f)