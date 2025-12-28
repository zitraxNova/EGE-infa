for n in range(0, 100):
	bin_n = bin(n)[2:]
	bin_n = bin_n + bin_n[-1]
	if bin_n.count('1') % 2 != 0:
		bin_n += '0'
	else:
		bin_n += '1'

	bin_n += '0'
	if int(bin_n, 2) > 413:
		print(int(bin_n, 2))
		
# 416