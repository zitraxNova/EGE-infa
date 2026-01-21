from itertools import *
k = 0
for x in product(sorted('ТЕОРИЯ'), repeat=5):
    s = ''.join(x)
    k += 1
    if k % 2 != 0 and s[0] not in 'РТЯ' and s.count('И') == 2:
        print(k, s)
        
# 43


