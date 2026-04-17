def f3(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s


def f3_n(n):
    f3_n = f3(n)
    if n % 3 == 0:
        f3_n += f3_n[-2:]
    else:
        f3_n += f3(sum(int(x) for x in f3_n))
    return int(f3_n, 3)


print(min(f3_n(x) for x in range(12, 200) if f3_n(x) > 220 and f3_n(x) % 2 == 0))

# 222