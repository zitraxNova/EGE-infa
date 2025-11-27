f = open('17_7596.txt')
a = []
for x in f:
    a.append(int(x))
print(a)
m = []
for i in range(len(a)):
    if str(a[i])[-1:] == '5' and len(str(abs(a[i]))) == 3:
        m.append(a[i])
m = min(m)
print(m)
res = []
for i in range(len(a) - 1):
    if (len(str(abs(a[i]))) == 3 and len(str(abs(a[i + 1]))) != 3) or (len(str(abs(a[i]))) != 3 and len(str(abs(a[i + 1]))) == 3):
        if (a[i] + a[i + 1]) % 5 == 0:
            res.append(a[i] + a[i + 1])
print(len(res), min(res))