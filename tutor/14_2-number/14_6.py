from string import *

for x in printable[:27]:
        d = int (f'8{x}38{x}68', 27) + int(f'37{x}3163', 27)
        if d % 26 == 0:
                print(d//26, x)