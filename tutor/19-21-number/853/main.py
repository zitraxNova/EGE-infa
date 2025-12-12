# 853
def f(n, s, m):
	if n + s >= 77:
		return m % 2 == 0
	if m == 0:
		return 0
	h = [f(n + 1, s, m - 1), f(n, s + 1, m - 1), f(n * 2, s, m - 1), f(n, s * 2, m - 1)]
	if m % 2 == 0:
		return all(h)
	else:
		return any(h)


print('#19')
for s in range(1, 69 + 1):
	if f(7, s, 2) == 1:
		print(s)

print('#20')
for s in range(1, 69 + 1):
	if f(7, s, 1) == 0 and f(7, s, 3) == 1:
		print(s)

print('#21')
for s in range(1, 69 + 1):
	if f(7, s, 2) == 0 and f(7, s , 4) == 1:
		print(s)




