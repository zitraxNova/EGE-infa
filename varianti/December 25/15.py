for a in range(-1000, 1000):
    f = 1
    for x in range(0, 1000): 
        for y in range(0, 1000): 
            if not ((x <= 19) or (y < 2 * x + a - 50) or (y > 17)):
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(a)
        break
# 28