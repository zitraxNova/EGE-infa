def f(st, fi):
    if st == 12:
        return 0
    if st > fi:
        return 0
    if st == fi:
        return 1
    return f(st + 1, fi) + f(st + 2, fi) + f(st * 2, fi)


result = f(2, 9) * f(9, 17)
print(result)
