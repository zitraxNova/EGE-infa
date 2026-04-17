from itertools import *
k = 0
for x in product(sorted('ЯНВАРЬ'), repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('Ь') <= 1 and s.count('ЯЯ') == 0 and s[0] != 'Я':
        print(k , s)
# 6406