def f(st, fi):
    if st > fi or st == 8 and st == 15:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 2, fi) + f(st * 3, fi)

print(f(3, 10) * f(10, 22))
# 5126