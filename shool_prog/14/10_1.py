from string import *

for x in printable[:17]:
    d = int(f'131{x}1', 15) + int(f'13{x}3', 17)
    if d % 11 == 0:
        print(d//11, x)
# 6101