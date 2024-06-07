## Zip unequal iterables 
## Input :
## List1 = [1,2,3]
## List2 = ['a','b']
## Output : [(1,'a'),(2,'b'),(3,None)]

from itertools import zip_longest
list1 = [1,2,3]
list2 = ['a','b']

zipped = zip_longest(list1,list2,fillvalue=None)

print(list(zipped))
