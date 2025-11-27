f = open('17_14256.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if str(a[i])[-2:] == '25':
                m.append(a[i])
m = max(m)
print(m)
res = []
for i in range(len(a) - 2):
        k = 0
        if sum(int(x) for x in str(abs(a[i]))) % 2 == 1:
                k += 1
        if sum(int(x) for x in str(abs(a[i+1]))) % 2 == 1:
                k += 1
        if sum(int(x) for x in str(abs(a[i+2]))) % 2 == 1:
                k += 1
        if k >= 2 and (a[i] + a[i+1] + a[i+2]) <= m:
                res.append(a[i] + a[i+1] + a[i+2])
print(len(res), max(res))
