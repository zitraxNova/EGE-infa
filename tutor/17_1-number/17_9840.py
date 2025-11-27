# 1 способ
f = open('17_9840.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if str(a[i])[-2:] == '39' and len(str(abs((a[i])))) == 4:     # a[i] % 100 == 39      10000<=abs(a[i]) >= 999
                m.append(a[i])
m = max(m)
print(m)
res = []
for i in range(len(a) - 1):
        k = 0
        if len(str(abs((a[i])))) == 4:
                k += 1
        if len(str(abs((a[i+1])))) == 4:
                k += 1
        if k == 1 and (a[i] + a[i + 1]) ** 2 <= m ** 2:
                res.append(a[i] + a[i + 1])
print(len(res), max(res))

        
