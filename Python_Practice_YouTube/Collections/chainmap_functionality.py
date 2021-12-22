dict1 = {'a':1,"b":3,"c":3}
dict2 = {'c':4,"d":8,"e":9}

from collections import ChainMap

new_dict = ChainMap(dict1,dict2)
print(new_dict['a'])

# Incase the value passed occured in both dictonaries.
# The value will be retained of the dictionary which is passed first in ChainMap

print(new_dict['c']) 