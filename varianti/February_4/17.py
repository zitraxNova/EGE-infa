file = open('17.txt').read().splitlines()
file = list(map(int, file))

max5 = max([x for x in file if x % 10 == 5 and 100 <= x <= 999])

maxS = -300_000
count = 0

for i in range(len(file)):
    three = file[i:i+3]
    three5 = len([x for x in three if x % 10 == 5])

    if (len(three) == 3 and three5 == 1 and sum(three) <= max5):
        count += 1
        maxS = max(maxS, sum(three))

print(count, maxS)