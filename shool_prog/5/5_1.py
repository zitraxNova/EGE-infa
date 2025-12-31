for n in range(10, 100):
 R = bin(n)[2:]
 if R.count('1') % 2 == 0:
  R += '0'
 else:
  R += '1'

 R += '0'
 if int(R, 2) > 180:
  print(int(R, 2))

# 184
