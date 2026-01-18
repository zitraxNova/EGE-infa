"""
# рекурсия 
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return (1)
	if st < fi:
		return f(st + 1, fi) + f(st * 3, fi)

		
print(f(1,20))



# аналитикой

	аналитикой	|	из какого получаем	|	кол-во програм	|
	1						-						1
	2						1						N2 = N1 = 1
	3						2, 1					N3 = N2 + N1 = 2
	4						3						2
	5						4						2
	6						5, 2					2 + 1 = 3
	...						...						...
	9						8, 3					3 + 2 = 5
	...						...						...
	12						11, 4					5 + 2 = 7
	...						...						...
	15						14, 5					7 + 2 = 9
	...						...						...
	18						17, 6					9 + 3 = 12
	
# Answer: 12
	


# аналитически
 
k = [1] * 21
for i in range(3, 21):
	if i % 3 == 0:
		k[i] = k[i - 1] + k[i // 3]
	else:
		k[i] = k[i - 1]
print(k[20])
"""
	
	
"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return (1)
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi)

		
print(f(1, 16))
# 36
"""


"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi) + f(st * 3, fi)

		
print(f(1,18))
# 96
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return (1)
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi) + f(st * 4, fi)

		
print(f(1,17))
# 54
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return (1)
	if st < fi:
		return f(st + 1, fi) + f(st * 3, fi) + f(st * 4, fi)

		
print(f(1,25))
# 38
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st + 2, fi) + f(st * 3, fi)
		
print(f(1, 12))
# 225
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 3, fi) + f(st * 2, fi)
		
print(f(3, 42))
# 26
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st % 2 == 0:
		return f(st + 1, fi) + f(st * 1.5, fi)
	else:
		return f(st + 1, fi)

print(f(1, 20))
# 32
"""


"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st % 2 == 0:
		return f(st + 1, fi) + f(st * 1.5, fi)
	else:
		return f(st + 1, fi)

print(f(1, 22))
# 44
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi) + f(2 * st + 1, fi)


print(f(2, 16))
# 40
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st + 2, fi)


print(f(5, 10) * f(10, 15))
# 64
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st + 3, fi)


print(f(3, 12) * f(12, 20))
# 247
"""

"""
def f(st ,fi):
	if st > fi:
		return 0 
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st + 2, fi) + f(st + 3, fi)
		
print(f(4,8) * f(8,15))
# 308
"""

"""
def f(st ,fi):
	if st > fi or st == 28:
		return 0 
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi) 
		
		
print(f(3, 10) * f(10, 34))
# 21
"""

"""
def f(st ,fi):
	if st > fi or st == 12:
		return 0 
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st * 2, fi) 
		
		
print(f(3, 20) * f(20, 30))
# 12
"""

"""
def f(st ,fi):
	if st > fi or st == 15:
		return 0 
	if st == fi:
		return 1
	if st < fi:
		return f(st + 1, fi) + f(st + 3, fi) 
		
		
print(f(2, 10) * f(10, 20))
# 156
"""

"""
def f(st, fi):
	if st < fi:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 2, fi) + f(st - 3, fi) + f(st ** (1/2), fi)
		
print(f(25, 3))
# 238
"""

"""
def f(st, fi):
	if st > fi:
		return 0
	if st == fi:
		return 1
	if st < fi:
		return f(st + 3, fi) + f(st * 2, fi) + f(st + 2, fi)
		
print(f(15, 61) * f(61, 64) * f(64, 80))
# 6500678
"""

"""
def f(st, fi):
	if st < fi or st == 9 or st == 16:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 1, fi) + f(st - 2, fi) + f(st // 3, fi)
		
print(f(19,3))
# 180
"""


"""
def f(st, fi):
	if st < fi or st == 23 and st == 20:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 3, fi) + f(st - 1, fi) + f(st - 4, fi)
		
print(f(43,17) - f(43, 23) * f(23,20) * f(20,17))
# 110445
"""

def f(st, fi):
	if st < fi:
		return 0
	if st == fi:
		return 1
	if st > fi:
		return f(st - 3, fi) + f(st - 4, fi)
		
print(f(44,19) - f(44, 33) * f(33,31) * f(31,19))

 
