f = open('17_17680.txt')
a = []
for x in f:
    a.append(int(x))
print(a)
m = []
for i in range(len(a)):
    if a[i] % 41 == 0:
        m.append(a[i])
m = min(m)
print(m)
res = []
for i in range(len(a) - 1):
            #.....
    print(len(res), max(res))