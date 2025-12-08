def f(n, s, m):
        if n + s >= 65:
                return m % 2 == 0
        if m == 0:
                return 0
        h = [f(n, s + 1, m - 1), f(n + 1, s,  m - 1) , f(n, s * 3, m - 1), f(n * 3, s, m - 1)] # перечень или списко допустимых ходов
        if m % 2 == 0:
                # true возвращается когда все истина, false во всех остальных случаях
                return any(h) # как функция и, true в остальных случаях
        else:
                return any(h) # как функция или, false back false
# m - номер хода, (1 - P I), (2 - V I), (3 - P II), (4 - V II)

print('#19')
for s in range(1, 59):
        if f(6,s, 2) == 1:
                print(s)

print('#20')
for s in range(1, 59):
        if f(6, s, 3) == 1 and f(6, s, 1) == 0:
                print(s)

print('#21')
for s in range(1, 59):
        if f(6, s, 4) == 1 and f(6, s, 1) == 0:
                print(s)
