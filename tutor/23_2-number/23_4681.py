def f(st, fi):
    if st > fi:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 3, fi) + f(st * 2, fi)


print(f(3, 27) * f(27, 63))

# 30