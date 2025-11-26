from string import *

for x in printable[:21]:
        d = int (f'82934{x}2',21) + int('2924' + x + x + '7',21) + int(f'67564{x}8', 21)
        if d % 20 == 0:
                print(d//20, x)