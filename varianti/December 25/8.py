from itertools import *
k = 0
for x in product(sorted('КОДИМ'), repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('М') == 2 and s.count('ММ') == 0:
        print(k, s)
        
# 3099


