from functools import *
@lru_cache(2000)
def f(x,y):
    if x + y >= 87:
        return 0
    hod = [f(x + 1,y), f(x * 2,y), f(x, y + 1), f(x, y * 2)]
    otr = [i for i in hod if i <= 0]
    if otr:
        return -max(otr) + 1
    else:
        return -max(hod)
for s in range(1,77):
    print(s, f(9,s))

# 19: 20; 20: 34 38; 21: 33
