# majority elements where it appears more than n/2 times
from collections import Counter
def majorityElement(nums):
    d=Counter(nums)
    for k,v in d.items():
        if v>len(nums)//2:
            return k
nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))
