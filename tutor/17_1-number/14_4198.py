# 1 способ
f = open('17_4198.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if a[i] % 21 == 0:
                m.append(a[i])
m = min(m)
print(m)
res = []
for i in  range(0, len(a) - 1):
        if (a[i] % m == 0) or (a[i + 1] % m == 0 ):
                                                      res.append(a[i] + a[i+1])
print(len(res), max(res))


# 2 способ
f = open('17_4198.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if a[i] % 21 == 0:
                m.append(a[i])
m = min(m)
print(m)
m = 100000000
for i in range(len(a)):
        if a[i] % 21 == 0:
                m = min(m, a[i])
print(m)
res = []
for i in  range(0, len(a) - 2):
        if (a[i] * a[i + 1] * a[i + 2]) % 7 == 0 and (a[i] + a[i+1] + a[i + 2]) % 10 == 5:
                                                      res.append(a[i] + a[i+1] + a[i + 2])
print(len(res), max(res))             
                                                      
