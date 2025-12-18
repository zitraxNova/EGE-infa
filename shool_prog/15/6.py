P = (list(range(10, 25)))
Q = (list(range(14, 40)))
A = []
for x in range(200):
    if not(x in A) and (not(x in P) <= (not(x in Q))):
        A.append(x)
print(len(A) - 1)
# 10