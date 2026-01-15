def f(n):
    if n > 15:
        return n ** 2 - 5
    if n <= 15:
        return n * f(n + 2) + n + f(n + 3)

res = f(1)
sum_digits = sum(int(digit) for digit in str(res))
print(sum_digits)

# 48