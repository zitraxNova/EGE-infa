from fnmatch import *

for n in range(0, 10 ** 8, 161):
    if fnmatch(str(n), '12*4?65') == 1:
        print(n, n // 161)
