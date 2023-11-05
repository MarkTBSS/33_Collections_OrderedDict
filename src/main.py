""" #sort by key
sortValue = OrderedDict(sorted(ordinaryDictionary.items()))
print(sortValue)
print("========================")
sortValue = OrderedDict(sorted(ordinaryDictionary.items(), reverse=True))
print(sortValue) """

from collections import OrderedDict

ordinaryDictionary = OrderedDict()
ordinaryDictionary['a'] = 1
ordinaryDictionary['b'] = 2
ordinaryDictionary['e'] = 5
ordinaryDictionary['d'] = 4
ordinaryDictionary['c'] = 3

print(ordinaryDictionary)
print(ordinaryDictionary['c'])

#sort by value
sortValue = OrderedDict(sorted(ordinaryDictionary.items(), key=lambda x: x[1]))
print(sortValue)
print("========================")
sortValue = OrderedDict(sorted(ordinaryDictionary.items(), key=lambda x: x[1], reverse=True))
print(sortValue)