from fnmatch import *
for x in range(0, 10**11+1, 98591):
    if fnmatch(str(x), '123*45??1?'):
         print(x, x//98591)


"""
1234457911 12521
12332452417 125087
"""