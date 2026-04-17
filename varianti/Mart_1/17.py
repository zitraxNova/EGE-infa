base = ''
nums = [int(x) for x in open(base + '17.txt')]
m43 = max([x for x in nums if 9999 < x < 100_000 and x % 100 == 43])**2
q = 0
min_sum = float('inf')
for tr in zip(nums, nums[1:], nums[2:]):
    if [x for x in tr if 9999 < abs(x) < 100_000 and abs(x) % 100 == 43] \
       and sum(x**2 for x in tr) <= m43:
        q += 1
        min_sum = min(min_sum, sum(x**2 for x in tr))
print(q, min_sum)

# 92  838850571