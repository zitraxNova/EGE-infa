s = open('24_28765.txt')
s = s.readline()

c = ''
m = 0
k = 0

for i in range(len(s)):
    c += s[i]
    if c[-2:] == 'BC':
        k += 1
    while k > 180:
        if c[:2] == 'BC':
            k -= 1
        c = c[1:]
    m = max(m, len(c))
    if i % 100000 == 0:
        print(i, len(s), m)
print(m)

