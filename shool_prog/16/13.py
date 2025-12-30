def f(n):
    if n >= 2022:
        return n
    if n < 2022:
        return 7 + f(n + 5)
    
res = f(45) - f(49)
print(res)

# 8