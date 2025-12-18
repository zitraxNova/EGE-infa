P = (list(range(15, 30)))
Q = (list(range(5, 60)))
A = []
for x in range(200):
    if (not(x in Q) or (x in P)) and (x in A):
        A.append(x)
print(len(A) - 1)
# -1