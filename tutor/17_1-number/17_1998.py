f = open('17_1998.txt')
a = []
for x in f:
        a.append(int(x))
print(a)
res = []
for i in  range(0, len(a) - 2):
        if (a[i] * a[i + 1] * a[i + 2]) % 7 == 0 and (a[i] + a[i+1] + a[i + 2]) % 10 == 5:
                                                      res.append(a[i] + a[i+1] + a[i + 2])
print(len(res), max(res))
                                                      
                                                      
