spisok = '0123456789A'

for x in spisok:
    for y in spisok:
        n = int(f'7{y}23{x}5', 25) + int(f'67{x}9{y}', 11)
        if n % 131 == 0:
            print(n // 131)
# 552647