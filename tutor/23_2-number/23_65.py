def f(st, fi):
    if st > fi:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 3, fi) + f(st * 2, fi)


print(f(3,9) * f(9,12) * f(12,20))

# 234