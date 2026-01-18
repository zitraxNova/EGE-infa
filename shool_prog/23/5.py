def f(x, y, st):
    if x == y and st[-2] == '2':
        return 1
    elif x > y or x == y and st[-2] == '1':
        return 0
    else:
        return f(x + 1, y, st + '1') + f(x + 2, y, st + '2')
print(f(3,18,''))
# 377