def f(st, fi):
    if st == 24:
        return 0
    if st < fi:
        return 0
    if st == fi:
        return 1
    if st > fi:
        return f(st - 1, fi) + f(st - 6, fi) + f(st // 2, fi)

print(f(34, 29) * f(29, 19) * f(19, 6))