def f(st, fi):
    if st > fi or st == 7:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 3, fi) + f(st * 2, fi)

print(f(2, 15) * f(15, 25))
# 2716