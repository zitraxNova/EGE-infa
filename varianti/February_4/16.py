def f(n):
    if n >= 2031:
        return 1
    if n < 2031:
        return n + 31 + f(n + 31)

res = f(31) - f(23)
print(res)
# 520
