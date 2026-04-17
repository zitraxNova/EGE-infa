from string import *

for x in printable[:25]:
    d = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if d % 24 == 0:
        print(d//24, x)
# 266249847