f = open('17.txt')  
a = [int(x) for x in f]  
c = sum([x for x in a if 10 <= abs(x) <= 99 and x % 2 == 0])
count, min_prod = 0, 10 ** 10 
for i in range(1, len(a)):  
    x, y = a[i - 1], a[i] 
    if (abs(x) % c == 0) != (abs(y) % c == 0):
        count += 1  
        min_prod = min(min_prod, x * y)  

print(count, abs(min_prod)) 