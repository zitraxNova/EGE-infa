from string import *

for x in printable[:19]:
        d = int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)
        if d % 18 == 0:
                print(d//18, x)