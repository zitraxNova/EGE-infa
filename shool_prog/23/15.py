def f(st, fi):
	if st < fi or st == 18:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 2, fi) + f(st  // 2 if st % 2 == 0 else st - 3, fi)

print(f(55, 3))
# 975