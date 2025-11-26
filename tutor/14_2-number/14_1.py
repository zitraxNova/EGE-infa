from string import *

for x in printable[:16]:
        d = int(f'9{x}AB', 13) + int(f'{x}46C', 16) - int(f'B7{x}', 15)
        if d % 14 == 0:
                print(d // 14, x)