# sort colors in place without using sort() or sorted()

from collections import Counter
def sortColors(nums):
    d=Counter(nums)
    nums2=list(set(nums))
    l=[]
    while nums2:
        s=min(nums2)
        l.extend([s]*d[s])
        nums2.remove(s)
    nums[:]=l
    return nums
nums=[0,2,1,1,2,0,0,2]
print(sortColors(nums))