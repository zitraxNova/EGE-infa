def f(st, fi):
    if st == 21:
        return 0
    if st > fi:
        return 0
    if st == fi:
        return 1
    return f(st + 1, fi) + f(st * 3, fi) + f(st * 4, fi)
print(f(2, 16) * f(16, 60))
# 40
