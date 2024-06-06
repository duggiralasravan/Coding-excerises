## Count values in the different list and print the each value and total count in each list 
## Example 
## Input
## L = ['a','b','a','c','b','a','b']
## NL = ['b','a','b','c','a','a']
## Output: {'a':6,'b': 5,'c':2}

from collections import Counter
L = ['a','b','a','c','b','a','b']
NL = ['b','a','b','c','a','a']

total_count = Counter(L)
print(total_count)

total_count.update(NL)
print(total_count)
