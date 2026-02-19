from itertools import *

k = 0
for i, w in enumerate(product('АБДЕОП', repeat=6), 1):
    if w[0] == 'О' and len(set(w)) == 6 and i % 2 == 0:
        k = i
print(k)
# 38306