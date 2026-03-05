from fnmatch import *

for n in range(0, 10 ** 8, 37):
    if fnmatch(str(n), '2*1234?6') == 1:
        print(n, n // 37)
