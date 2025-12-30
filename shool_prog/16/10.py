def f(n):
    if n > 15:
        return n ** 2 - 5
    if n <= 15:
        return n * f(n + 2) + n + f(n + 3)
    
print(f(1))
# 884415846