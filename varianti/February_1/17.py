f = open('17_1.txt')
a = []
for x in f:
    a.append(int(x))
print(a)

m = []
for i in range(len(a)):
    if a[i] > 0 and 999 < a[i] < 10000 and a[i] % 10 == 6:
        m.append(a[i])
m = min(m)
print(m)

res = []
for i in range(len(a) - 2):
    count = 0
    if 999 < abs(a[i]) < 10000 and abs(a[i]) % 10 == 6:
        count += 1
    if 999 < abs(a[i + 1]) < 10000 and abs(a[i + 1]) % 10 == 6:
        count += 1
    if 999 < abs(a[i + 2]) < 10000 and abs(a[i + 2]) % 10 == 6:
        count += 1
        
    if count == 1:
        s = a[i] + a[i + 1] + a[i + 2]
        if s <= m:
            res.append(s)

print(len(res), max(res))
