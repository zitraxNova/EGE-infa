n = (7**160 * 7**90) - (14**150 + 2**13)
digits = []
while n > 0:
    digits.append(n % 7)
    n = n // 7
sum_digits = sum(d for d in digits if d != 6)
print(sum_digits)
# 145