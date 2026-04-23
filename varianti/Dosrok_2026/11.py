from math import *
kod = 10 + 1015
bit = ceil(log2(kod))
idd = ceil(289 * bit /8)
res = 524288 * idd / 1024 / 1024
print(res)
# 199