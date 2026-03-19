from math import dist  

def centr(cluster):
    res_dist = 0
    res_centr = 0
    for i in cluster:
        cur = sum(dist(k, i) for k in cluster if k != i)
        if cur > res_dist:
            res_dist = cur
            res_centr = i
    return res_dist, res_centr[0], res_centr[1]
f = open('27B.txt')
a = [list(map(float, x.split())) for x in f]
cl = [[], [], [], [], []]
for st in a:
    x, y = st
    if x < -10 and 0 < y < 20:
        cl[0].append((x, y))
    elif -10 < x < 10 and y > 20:
        cl[1].append((x, y))
    elif 10 < x < 20 and y > 23:
        cl[2].append((x, y))
    elif 0 < x < 23 and 13 < y < 23:
        cl[3].append((x, y))
    elif x > 23 and 0 < y < 13:
        cl[4].append((x, y))
px, py = 0, 0
maxi = 0
for i in cl:
    sumi, x, y = centr(i)
    if sumi > maxi:
        maxi = sumi
        px, py = x, y
print(int(abs(px) * 10000), int(abs(py) * 10000))  