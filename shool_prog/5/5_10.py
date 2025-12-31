for n in range(0, 100):
    last_digit = n % 10 
    n = int(str(n) + str(last_digit))
    bin_n = bin(n)[2:]  
    bin_n += '1'  
else:
    bin_n += '0' 
bin_n += '0'  
    
result = int(bin_n, 2)
if result > 413:  
        print(result)
        

# 7996
