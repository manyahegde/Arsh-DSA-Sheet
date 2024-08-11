# Find the duplicate number
from collections import Counter
def FindDuplicate(nums):
    d=Counter(nums)
    for key,value in d.items():
        if value>1:
            return key
nums=[1,3,4,4,2]
print(FindDuplicate(nums))