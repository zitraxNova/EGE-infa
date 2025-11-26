res = []
for x in range(1 ,3000 +1):
        n = 4 ** 210 + 4 ** 110 - x
        k = 0
        while n > 0:
                d = n % 4
                if d == 0:
                        k += 1
                n = n // 4
        res.append((k, x)) # в массив результатов сохраняем кол-во полученых нулей и соответсвующие x
res = sorted(res)
print(res)
               