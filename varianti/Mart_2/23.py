def f(st, fi):
    if st > fi:
        return 0
    if st == fi:
        return 1
    if st < fi:
        return f(st+3, fi) + f(st+5, fi) + f(st*2, fi)

print(f(4, 14) * f(14, 31))
print(f(4, 19) * f(19, 31))
print(f(4, 14) * f(14, 19) * f(19, 31))
# 22