def f(st, fi):
    if st > fi or st == 10:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st+1, fi) + f(st+2, fi) + f(st*2, fi)


print(f(3, 7) * f(7, 20))

# 792
