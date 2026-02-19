f = open('24_21597.txt')
s = f.readline()
for t in '6789':
    s = s.replace(t, '#')

m = 0
for lt in range(len(s)):
    for rt in range(lt + m + 1, len(s)):
        a = s[lt:rt]
        if a[0] in '*-0' or a.count('#') > 0 or '--' in a or '*-' in a or '-*' in a or '**' in a:
            break
        if a[0] not in '0' and a.count('#') == 0 and a not in ['--','*-','-*','**']:
            m = max(m, len(a))
            print(a)
print(m)
