def f(st, fi):
    if st > fi or st == 11 or st == 18:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st + 1, fi) + f(st + 2, fi) + f(st * 3, fi)    
print(f(4, 8) * f(8, 23))
# 400