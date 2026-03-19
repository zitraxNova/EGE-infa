from itertools import product

alph = '0123456789ABC'
even = alph[::2]
deny = [''.join(p) for p in product(even, 'ABC')] + [''.join(p) for p in product('ABC', even)]
q = 0

for p in product(alph, repeat=6):
    num = ''.join(p)
    q += num[0] != '0' and num.count('1') == 2 and all(''.join(c) not in deny for c in zip(num, num[1:]))
print(q)