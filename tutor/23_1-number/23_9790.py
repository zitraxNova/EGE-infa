def f(st, fi):
    if st < fi or st == 9 or st == 16:
        return 0
    if st == fi:
        return 1
    if st > fi:
        return f(st - 1, fi) + f(st - 2, fi) + f(st // 3, fi)


print(f(19,3))

# 180