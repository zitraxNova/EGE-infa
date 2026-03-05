from fnmatch import *

for n in range(0, 10 ** 8, 2025):
    if fnmatch(str(n), '12*34?5') == 1:
        print(n, n // 2025)
