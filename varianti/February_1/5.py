def f3(x):
    s = ''
    while x:
        s += str(x % 3)
        x = x // 3
    return s[::-1]

for n in range(3, 100):
    f3_n = f3(n)
    if n % 3 == 0:
        f3_n += f3_n[-2:]
    else:
        f3_n += f3((n % 3) * 3)

    if int(f3_n, 3) < 150:
        print(n)
# 16