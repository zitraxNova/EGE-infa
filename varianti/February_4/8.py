from itertools import product
digits = '0Н234Н6'
count = 0
for nums in product(digits, repeat=6):
    number = ''.join(nums)
    if (number[0] != '0' and number.count('3') == 1 and
        'НН' not in number and '3Н' not in number and 'Н3' not in number):
        count += 1

print(count)

# 16448