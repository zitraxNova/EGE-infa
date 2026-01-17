def f(st, fi):
    if st < fi:
        return 0
    if st == fi:
        return 1
    if st > fi:
        return f(st - 2, fi) + f(st - 4, fi) + f(st ** (1/2), fi)

print(f(46, 32) * f(32, 12) * f(12, 2))
# 24297