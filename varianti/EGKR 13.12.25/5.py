def f3(x):
	s = ''
	while x > 0:
		s = str(x % 3) + s
		x = x // 3
	return s


m = []
for n in range(1, 1000):
	f3_n = f3(n)
	if n % 3 == 0:
		f3_n = f3_n + f3_n[-2] + f3_n[-1]
	else:
		f3_n = f3_n + f3(sum(map(int, f3_n)) * 3)
	r = int(f3_n, 3)
	if r % 2 != 0 and r > 208:
		m.append(r)
print(min(m))
# 243