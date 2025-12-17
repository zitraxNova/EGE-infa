def f(st, fi):
    if st == 36:
        return 0
    if st < fi:
        return 0
    if st == fi:
        return 1
    return f(st - 3, fi) + f(st - 6, fi) + f(st // 2, fi)


print(f(86, 53) * f(53, 12))
