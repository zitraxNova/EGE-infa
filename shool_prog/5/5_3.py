for n in range(500, 1000):
 bin_n = bin(n)[2:]
 bin_n = bin_n[::-1]
 if int(bin_n, 2) == 19:
  print(n)
# 800