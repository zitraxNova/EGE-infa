def f(n, s, m):
    if n + s >= 65:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, n, m - 1), f(s, n + 1, m - 1), f(s * 3, n, m - 1), f(s, n * 3, m - 1)]
    if m % 2 == 0:
        return all(h)
    else:
        return any(h)

print('#19')
for s in range(1, 58 + 1):
    if f(6, s, 2) == 1:
        print(s)
# 7
print('#20')
for s in range(1, 58 + 1):
    if f(6, s, 1) == 0 and f(6, s, 3) == 1:
        print(s)
# 10 19
print('#21')
for s in range(1, 58 + 1):
    if f(6, s, 2) == 0 and f(6, s, 4) == 1:
        print(s)
# 18

