def f (st,fi): 
        if st == fi: 
                return 1 
        if st < fi or st == 24: 
                return 0 
        return f(st//2, fi) + f(st - 1, fi) + f(int(st ** 0.5),fi) 
print(f(602,7))

