def f(st, fi):
    if st < fi or st == 13:
        return 0
    if st == fi:
        return 1
    else:
        return f(st - 1, fi) + f(st - 2, fi) + f(st // 3, fi)


print(f(19, 6) * f(6, 4))
# 212