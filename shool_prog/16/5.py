def f(n):
    global s
    s += n - 5
    if n > 1:
        s += n + 8
        f(n - 2)
        f(n - 3)
    return s
for n in range(1, 100):
    s = 0 
    if f(n) > 3200000:
        print(n, f(n))
        break

# 46 6535702
        