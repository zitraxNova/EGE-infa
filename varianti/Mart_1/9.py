f = open('9.txt') 
data = [list(map(int, i.split())) for i in f]

def f1(line):
    cnt_3 = [i for i in line if line.count(i) == 3]
    cnt_1 = [i for i in line if line.count(i) == 1]
    return len(cnt_3) == 6 and len(cnt_1) == 1

def f2(line):
    nrep = [i for i in line if line.count(i) == 1]
    rep = [i for i in line if line.count(i) != 1]
    aver = sum(rep) / len(rep)
    return aver < nrep[0]

for pos, val in list(enumerate(data, start=1))[::-1]:
    if f1(val) and f2(val):
        print(pos)
        break

# 17975