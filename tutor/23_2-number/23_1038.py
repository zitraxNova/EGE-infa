def f(st, fi):
    if st > fi or st == 8:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 2, fi) + f(st * 3, fi)


print(f(2, 50) * f(50, 60))

# 6