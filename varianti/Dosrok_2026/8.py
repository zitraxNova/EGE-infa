from itertools import *

k = 0
for x in product(sorted('АПРЕЛЬ'), repeat=5):
    s = ''.join(x)
    k += 1
    if k % 2 == 0 and s[0] not in 'ЬР' and s.count('Л') >= 2:
        print(k, s)

# 5058 ПЬЛЛЬ