# find duplicates
from collections import Counter
def findDuplicates(nums):
    d=Counter(nums)
    result=[]
    for k,v in d.items():
        if v>1:
            result.append(k)
    return result
nums=[4,3,2,7,8,2,3,1]
print(findDuplicates(nums))