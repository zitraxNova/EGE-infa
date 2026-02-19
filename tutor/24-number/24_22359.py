f = open('24_22359.txt')
s = f.readline()
for i in range(70, 91):
    s = s.replace(chr(i), '*')
m = 0
for lt in range(len(s)):
    for rt in range(lt + m + 1, len(s)):
        a = s[lt:rt]
        if a.count('*') > 0 or a[0] == '0':
            break
        if a.count('*') == 0 and a[0] != '0' and int(a, 15) % 5 == 0:
            m = max(m, len(a))
            if m == 112:
                print(a,lt, rt)
print(m)
