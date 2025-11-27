f = open('17_17558.txt')
a = []
for x in f:
    a.append(int(x))
print(a)

m = []
for i in range(len(a)):
    if a[i] % 32 == 0:
        m.append(a[i])
m = len(m)
print(m)
res = []
for i in range(len(a) - 1):
    k = 0
    if a[i] < 0:
        k += 1
    if a[i + 1] < 0:
        k += 1
    if k >= 1 and (a[i] + a[i + 1]) < m:
        res.append(a[i] + a[i + 1])
print(len(res), max(res))
