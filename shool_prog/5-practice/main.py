"""
for n in range(10, 100):
	R = bin(n)[2:]
	R += str(R.count('1') % 2)
	R += str(R.count('1') % 2)
	if int(R, 2) > 137:
		print(n)
# 35
"""

"""
for n in range(10, 50):
	R = bin(n)[2:]
	if R.count('1') % 2 == 0:
		R += '0'
	else:
		R += '1'
		
	R += '0'
	if int(R, 2) > 103:
		print(n)
# 26
"""

"""
for n in range(0, 100):
	bin_n = bin(n)[2:]
	bin_n = bin_n + bin_n[-1]
	if bin_n.count('1') % 2 == 0:
		bin_n += '0'
	else:
		bin_n += '1'
		
	bin_n += '0'
	if int(bin_n, 2) > 80:
		print(int(bin_n, 2))
# 92
"""

"""
for n in range(0, 500):
	bin_n = bin(n)[2:]
	bin_n = bin_n[::-1]
	if int(bin_n, 2) == 13:
		print(n)
# 352
"""

"""
for n in range(10, 100):
	bin_n = bin(n)[2:]
	bin_n = bin_n + bin_n[-2] + bin_n[1]
	if int(bin_n, 2) > 170:
		print(n)
# 43
"""

"""
for n in range(66, 100):
	bin_n = bin(n)[2:]
	if bin_n.count('1') == bin_n.count('0'):
		bin_n += bin_n[-1]
	elif bin_n.count('1') > bin_n.count('0'):
		bin_n += '0'
	else:
		bin_n += '1'
		
	if bin_n.count('1') == bin_n.count('0'):
		bin_n += bin_n[-1]
	elif bin_n.count('1') > bin_n.count('0'):
		bin_n += '0'
	else:
		bin_n += '1'
		
	if bin_n.count('1') == bin_n.count('0'):
		bin_n += bin_n[-1]
	elif bin_n.count('1') > bin_n.count('0'):
		bin_n += '0'
	else:
		bin_n += '1'
		
	if int(bin_n, 2) % 4 == 0:
		print(n)
"""

"""
for n in range(0,10000):
	bin_n = bin(n)[2:]
	if n % 2 == 0:
		bin_n = '1' + bin_n + '11'
	else:
		bin_n = '11' + bin_n + '00'
		
	if int(bin_n, 2) < 127:
		print(int(bin_n,2))
# 124
"""

def f3(x):
	s = ''
	while x:
		s += str(x % 3)
		x = x // 3
	return s[::-1]	
for n in range(1,100):
	f3_n  = f3(n)
	if n % 3 == 0:
		f3_n += f3_n[-2:]
	else:
		f3_n += f3(n % 3 * 3)	
	if int(f3_n,3) < 150:
		print(n) 
		
		
	
	
	
