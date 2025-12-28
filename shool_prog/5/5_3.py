for n in range(0, 500):
 bin_n = bin(n)[2:]
 bin_n = bin_n[::-1]
 if int(bin_n, 2) == 19:
  print(n)
# 25