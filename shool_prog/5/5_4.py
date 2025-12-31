for n in range(10, 100):
    R = bin(n)[2:]
    if R.count('1') % 2 == 0:
        R += '11'  
    else:
        R += '11' 
    R += '0' 
    if int(R, 2) > 412:
        print(n)
# ???