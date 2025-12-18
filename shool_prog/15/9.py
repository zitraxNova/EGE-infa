P = (list(range(15, 30)))
Q = (list(range(5, 60)))
R = (list(range(35, 50)))
A = []
for x in range(200):
    if ((x in P) <= (x in Q)) or (not(x in A) <= (x in R)):
        A.append(x)
print(len(A) - 1)
# 199
