s = open("24.txt").readline() 
s = s.replace(". ", ".")  
s = s.split(".") 
maxi = 0 
for i in s: 
    if '  ' in i:  
        i = i.split('  ')[-1]  
    while len(i) > 0 and i[0] not in "LND":  
        i = " ".join(i.split()[1:])
    if len(i) > 0: 

        if all("L" not in j[1:] and "N" not in j[1:] and "D" not in j[1:] for j in i.split()):
     
            if len(list(set([j for j in i.split() if i.split().count(j) > 1]))) <= 2:
                i += '.'  
                maxi = max(maxi, len(i))  
print(maxi)  