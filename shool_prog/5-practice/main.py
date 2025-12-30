
"""
# 1 task 
# 1 way
f = [0] * 10
for n in range(10):
	f[n] = 1
	if n > 1:
		f[n] = f[n-1] * n
		
print(f[5])
"""

"""
# 1 task 
# 2 way
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) * n
		
		
print(f(5))
"""

"""
# 2 task
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) * (n + 1)
		
		
print(f(5))
"""

"""
# 3 task
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) * (n + 2)
		
		
print(f(5))
"""

"""
# 4 task
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) * (2 * n + 1)
		
		
print(f(4))
"""

"""
# 5 task 
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) * (2 * n - 1)
		
		
print(f(5))
"""

"""
# 6 task
def f(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return n + 2 + f(n -1)
	else:
		return 2 * f(n - 2)
		
		
print(f(24))
"""


"""
def f(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) - 2 * g(n - 1)
def g(n):
	if n == 1:
		return 1
	if n > 1:
		return f(n - 1) + 2 * g(n - 1)
		
print(g(21))
"""

"""
def f(n):
	global k
	k += 1
	if n >= 1:
		k += 1
		f(n - 1)
		f(n - 2)
	return k  
k = 0
print(f(28))
"""

"""
def f(n):
	global k
	k += 1
	if n >= 1:
		k += 1
		f(n - 1)
		f(n - 2)
		k += 1
	return k
		
k = 0
print(f(35))
"""

"""
def f(n):
	global s
	s += n + 1
	if n > 1:
		s += n + 5 
		f(n - 1)
		f(n - 2)
	return s
for n in range(1, 100):
	s = 0	
	if f(n) > 1000000:
		print(n, f(n))
		break
"""

"""
def f(n):
	if n > 20:
		return n**3 + n
	if n % 2 == 0 and n <= 20:
		return 3 * f(n + 1) + f(n + 3)
	else:
		return f(n + 2) + 2 * f(n + 3)
		
k = 0
for n in range(1, 1000+1):
	s = str(f(n))
	if s.count('1') == 0:
		k += 1
print(k)
"""

"""
def f(n):
	if n > 30:
		return n * n + 3 * n + 5
	if n % 2 == 0 and n <= 30:
		return 2 * f(n + 1) + f(n + 4)
	else:
		return f(n + 2) + 3 * f(n + 5)
		
k = 0
for n in range(1, 1000+1):
	s = str(f(n))
	if s.count('0') >= 2:
		k += 1
print(k)
"""

"""
f = [0] * 2500
for n in range(2500):
	if n == 1:
		f[n] = 1
	if n > 1:
		f[n] = n * f[n - 1]
		
res = f[2023] // f[2020]
print(res)
"""

"""
from sys import *
setrecursionlimit(6000)
def f(n):
	if n <= 10:
		return n
	if n >= 10000:
		return 1
	if 10 < n < 10000 and n % 2 == 0:
		return n % 10 + f(n + 2)
	else:
		return f(n - 2) - (n - 1) % 10
		
res = f(4500) + f(5515)
print(res)
"""

from sys import *
setrecursionlimit(3500)
def f(n):
	if n >= 3210:
		return 1
	if n < 3210:
		return f(n + 3) + 7
def g(n):
	if n < 10:
		return n
	if n >= 10:
		return g(n - 3) + 5
		
res = f(15) - g(3000)
print(res)