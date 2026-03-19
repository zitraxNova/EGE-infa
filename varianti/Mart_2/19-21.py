def f(s, m):
    if s >= 627:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 3, m - 1), f(s + 4, m - 1), f(s ** 2, m - 1)]
    if m % 2 == 0:
        return all(h)
    else:
        return any(h)


print('#19')
for s in range(1, 200 + 1):
    if f(s, 2) == 1:
        print(s)

print('#20')
for s in range(1, 200 + 1):
    if f(s, 1) == 0 and f(s, 3) == 1:
        print(s)

print('#21')
for s in range(1, 64 + 1):
    if f(s, 2) == 1 and f(s, 1) == 0:
        print(s)

# 19  23
# 20  5 19
# 21  25