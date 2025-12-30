def F(n):
  if n > 0: 
    return n % 10 * F(n // 10)
  else: return 1

for n in range(1, 100000):
    if F(n) > 320:
        print(n, F(n))
        break

# 499 324