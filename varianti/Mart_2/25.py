def prost(x): 
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True 


def count_r(x): 
    r = 0 
    for i in range(2, int(x ** 0.5) + 1): 
        if x % i == 0: 
            if not prost(i): r += i 
            if not prost(x // i): r += x // i 
    return r 
c = 987653 
count = 0 
while True: 
    c -= 1 
    if count_r(c) % 10 == 7: 
        print(c) 
        count += 1 
    if count == 5: 
        break 