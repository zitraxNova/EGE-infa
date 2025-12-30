def f(n):
    global k 
    k += 1
    if n < 6:
        f(n + 1)
        f(n + 2)
        f(n * 2)
    return k
k = 0 
print(f(1))
# 70