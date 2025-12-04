def f(n):
        if n == 1:
                return 1
        if n % 2 == 0:
                return n + f(n-1)
        if n % 2 != 0:
                return 2 * f(n-2)
a = f(26)
print(a)
# 4122