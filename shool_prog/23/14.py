def f(st, fi):
	if st < fi or st == 33 and st == 31:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 3, fi) + f(st - 4, fi)

print(f(44,19))
# 43