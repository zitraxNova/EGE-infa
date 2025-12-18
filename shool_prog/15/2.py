def Del(x):
    return (x % 18 == 0) <= ((x % a != 0) <= (x % 12 != 0))


for a in range(1, 1000):
    if all(Del(x) == 1 for x in range(1, 100000)):
        print(a)

# 36

"""
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if (x % 18 == 0) <= ((x % a != 0) <= (x % 12 != 0)):
            k += 1
    if k == 999:
        print(a)
        break
"""


