spisok = '123456789ABCDE'

for x in spisok[::-1]:
    d = int(f'131{x}1', 15) + int(f'13{x}3', 17)
    if d % 11 == 0:
        print(d//11, x)
#6101
