def f(st, fi):
    if st > fi:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 3, fi) + f(st + 6, fi)

print(f(21, 30))
# 25