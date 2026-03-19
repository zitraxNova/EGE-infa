from functools import *
def f(n):  
    if n > 10000:
        return 2025
    elif n % 2 != 0:
        return f(3*n + 1) + n + 1
    else:
        return f(n+3) + 2*n + 3

for n in range(10000, 20, -1): 
    f(n)  
print(2*f(25) - f(238)) 