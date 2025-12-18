P = (list(range(10, 50)))
Q = (list(range(35, 45)))
A = []
for x in range(200):
    if (not(x in P) <= (x in Q)) and (not(x in A)):
        A.append(x)
print(len(A) - 1)
# 29  