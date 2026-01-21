a = []
for n in range(1, 100):
    R = bin(n)[2:]
    R = str(R)
    if n % 2 == 0:
        R = "10" + R
    else:
        R = "1" + R + "01"
    r = int(R, 2)
    if r < 30:
        a.append(n)
print(max(a))
# 6