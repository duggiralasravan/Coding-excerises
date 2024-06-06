## Provided a list of integers , find the subsets sum that matches to a given number    
###################################################################################
## Example
## Input : a=[2,4,5,6,8,10] , sum_value =10
## Output : [(2, 8), (4, 6)]

from itertools import chain, combinations
a=[-1,-3,2,4,5,6,8,10]
sum_value = 12
x = chain.from_iterable(combinations(a, r) for r in range(len(a)+1)) 
subsetList = list(x)
print([(x) for x in subsetList if sum(x) == sum_value])
