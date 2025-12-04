def f(st, fi):
    if st == fi:
        return 1
    if st > fi or st == 56:
        return 0
    return f(st + 3, fi) + f(st + 7, fi) + f(st * 3, fi)


print(f(12, 40) * f(40, 72) * f(72, 89))
# 324