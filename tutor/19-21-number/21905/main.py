def f(s, m):
        if s >= 67:
                return m % 2 == 0
        if m == 0:
                return 0
        h = [f(s + 1, m - 1), f(s + 4, m - 1) , f(s * 3, m - 1)] # перечень или списко допустимых ходов
        if m % 2 == 0:
                # true возвращается когда все истина, false во всех остальных случаях
                return all(h) # как функция и, true в остальных случаях
        else:
                return any(h) # как функция или, false back false
# m - номер хода, (1 - P I), (2 - V I), (3 - P II), (4 - V II)

print('#19')
for s in range(1, 67):
        if f(s, 2) == 1:
                print(s)

print('#20')
for s in range(1, 67):
        if f(s, 3) == 1 and f(s, 1) == 0:
                print(s)

print('#21')
for s in range(1, 67 ):
        if f(s, 4) == 1 and f(s, 1) == 0:
                print(s)
