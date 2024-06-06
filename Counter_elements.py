## List of alphabets that contains random alphabets in random order
## Arrange the same alphbets together in the order of insertion 

Example:
Input 
L = ['a','c','a','b','b','a','c']
Output 
['a','a','a','c','c,','b','b']

from collections import Counter

L = ['a','c','a','b','b','a','c']
print(list(Counter(L).elements()))
