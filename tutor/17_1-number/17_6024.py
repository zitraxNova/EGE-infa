# 1 способ
f = open('17_6024.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if str(a[i])[-2:] == '12':      # a[i] % 100 == 12
                m.append(a[i])
m = max(m)
print(m)
res = []
for i in range(len(a) - 1):
        k = 0
        if str(a[i])[-2:] == '12':
                k += 1
        if str(a[i+1])[-2:] == '12':
                k += 1
        if k == 1 and (a[i] + a[i + 1]) ** 2 < m ** 2:
                res.append(a[i] + a[i + 1])
print(len(res), max(res))

        
