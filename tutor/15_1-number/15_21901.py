def f(x):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (x & a != 0)
for a in range(100):
    if all(f(x) == 1 for x in range(1000)):
        print(a)
        break