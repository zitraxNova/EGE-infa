def f(n):
    global k
    k += 1
    if n < 6:
        f(n + 1)
        f(n + 2)
        f(n * 2)
    return k
k = 0
res = f(1)
sum_digits = sum(int(digit) for digit in str(res))
print(sum_digits)
# 7 