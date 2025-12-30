from itertools import * 
k = 0 
for x in product(sorted('ГРАНИТ'), repeat=6):
    s = ''.join(x)
    k += 1
    if k % 2 != 0 and s[0] not in 'АИГ' and s.count('А') == 1:
        print(k, s)
        break
# 23589