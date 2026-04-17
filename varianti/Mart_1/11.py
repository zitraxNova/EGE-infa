
from math import ceil

x = 1
while ceil(377 * x / 8) * 23_155 <= 5536 * 2**10:
    x += 1

print(2**(x - 1) + 1)

# 33