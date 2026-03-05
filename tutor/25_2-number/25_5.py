from fnmatch import *

for n in range(0, 10 ** 9, 17):
    if fnmatch(str(n), '12345?57?8') == 1:
        print(n, n // 17)
