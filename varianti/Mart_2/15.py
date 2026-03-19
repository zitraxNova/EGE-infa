def expr(x, y, A):
    return (x < 25) <= ((x > 3 * y) <= (A > 4 * x * y))

for A in range(1, 1000):
    if all(expr(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
    