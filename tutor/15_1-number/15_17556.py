b = list(range(70, 90 + 1))
for a in range(1000,1,-1):
    f = 1
    for x in range (1,1000):
        if ((x%a==0) or ((x in b) <= (not(x%22==0)))) == False:
            f = 0
            break
    if f == 1:
        print(a)
        break