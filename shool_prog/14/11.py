first_digit = '55113x'
second_digit = '7xx580'
k = 0
for x in range(0, 100000):
    if abs(int(first_digit.replace('x', str(x))) - int(second_digit.replace('xx', str(x)))) < 1000000:
        k += 1
print(k)
# 10