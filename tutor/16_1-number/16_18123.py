f = [0] * 2500
for n in range(2500):
    if n >= 2010:
        f[n] = n
    if n < 2010:
        f[n] = f[n+3] + f[n+2] + f[n+1]
print((f[2000] - 2 * (f[2002] + f[2003])) // f[2004])


def f(n):
    if n >= 2010:
        return n
    if n < 2010:
        return f(n+3) + f(n+2) + f(n+1)
print(f(2000) - 2 * (f(2002) + f(2003))) // f(2024)
    
# ???
