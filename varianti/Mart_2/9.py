res = 0  
for line in open('9.csv'): 
    nums = [int(x) for x in line.strip().split(';')]
    if len(nums) != len(set(nums)): 
        rep_3 = [x**2 for x in nums if nums.count(x) == 3]
        rep_sum = sum([x for x in rep_3])
        non_rep = [x for x in nums if nums.count(x) == 1]
        non_rep_sum = sum(non_rep) ** 2
        if rep_sum >= non_rep_sum:
            res = sum(nums)  
print(res) 