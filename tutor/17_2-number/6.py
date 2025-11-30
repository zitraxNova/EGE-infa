f = open('17_6.txt')
a = []
for x in f:
    a.append(int(x))
print(a)
m = []
for i in range(len(a)):
    if a[i] % 10 == 8: 
        m.append(a[i])
m = min(m)              
print(m)
res = []
for i in range(len(a) - 1):
    k = 0
    if a[i] % 16 == m:
        k += 1
    if a[i+1] % 16 == m:
        k += 1
    if k == 1:
        res.append(a[i] + a[i+1])
print(len(res), max(res))