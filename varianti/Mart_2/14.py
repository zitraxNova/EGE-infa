n = 7 * 729**2048 + 3 * 243**1413 - 7 * 81**169 - 3 * 9**107 + 2017
s = 0
while n:
    dig = n % 27
    s += dig if dig > 17 else 0
    n //= 27
print(s)