f = open('24_1.txt')
s = f.readline()
m = 1

for lt in range(0, len(s)):
    for rt in range(lt + m + 1, len(s)):
        a = s[lt:rt]
        if a.count('RSQ') > 130:
            break
        if a.count('RSQ') == 130 and a[0] != 'Q':
            m = max(m, len(a))
print(m)
# 701