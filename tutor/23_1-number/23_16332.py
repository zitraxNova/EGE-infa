def f(st, fi):
    if st > fi:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 2, fi) + f(st * 2, fi)


print(f(4,11) * f(11, 13) * f(13, 15))
# 100