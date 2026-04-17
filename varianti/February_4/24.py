file = open('24.txt').read()

chain = 'FSWY'

while chain + 'FSWY' in file:
    chain += 'FSWY'

chain = 'SWY' + chain + 'FSW'
print(chain in file)
print(len(chain))

# 186