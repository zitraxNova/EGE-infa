for n in range(1, 1000):
    bin_n = bin(n)[2:]  
    sum_digits = sum(int(i) for i in bin_n) 
    if sum_digits % 2 == 0: 
        bin_n = '10' + bin_n  
    else:
        bin_n = '11' + bin_n  

    r = int(bin_n, 2)  
    if r < 35: 
        print(n) 
# 7
         