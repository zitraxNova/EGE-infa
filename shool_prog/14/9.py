from string import *

for x in printable[:13]:
    d = int(f'8{x}121', 13) - int(f'7{x}575', 13)
    if d % 19 == 0:
        print(d // 19, x)
# 1464