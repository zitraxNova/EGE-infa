def f(st, fi):
    if st == fi:
        return 1
    if st < fi:
        return 0
    return f(st // 2, fi) + f(st - 2, fi)


print(f(28, 10) * f(10, 1))  # обязательное число 10

# 36