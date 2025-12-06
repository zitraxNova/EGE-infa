def f(st, fi):
    if st > fi or st == 11:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st * 2, fi) + f(st ** 2, fi)


print(f(2, 20))

# 37