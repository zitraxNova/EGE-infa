# 1 способ
f = open('17_17636.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
m = []
for i in range(len(a)):
        if str(a[i])[-1:] == '3' and len(str(abs((a[i])))) == 3:     # a[i] % 10 == 3       999 >=abs(a[i]) >= 100
                m.append(a[i])
m = max(m)
print(m)
res = []
for i in range(len(a) - 2):
        k = 0
        if str(a[i])[-1:] == '3' and len(str(abs((a[i])))) == 3:
                k += 1
        if str(a[i+1])[-1:] == '3' and len(str(abs((a[i+1])))) == 3:
                k += 1
        if str(a[i+2])[-1:] == '3' and len(str(abs((a[i+2])))) == 3:
                k += 1
        
        if k > 0 and (a[i] + a[i + 1] + a[i + 2]) < m:
                res.append(a[i] + a[i + 1] + a[i + 2])
print(len(res), max(res))

        
