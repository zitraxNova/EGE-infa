f = open('24_1.txt').readline()
parr = []
p = 0
ls = len(f)
while p < ls:
    if f[p:p+3] == 'RSQ':
        parr.append(p)
        p += 3
    else:
        p += 1
min_sim = float('inf')
for x, y in zip(parr, parr[129:-1]):
    y += 2
    while f[y] == 'Q':
        y += 1
    min_sim = min(min_sim, y - x + 1)
x, y = parr[-130], parr[-1] + 2
while y < ls and f[y] == 'Q':
    y += 1
if y < ls:
    min_symb = min(min_sim, y - x + 1)
print(min_sim)
