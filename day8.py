# two sum
def twoSum(nums, target):
    d={}
    for i,n in enumerate(nums):
        if target-n in d:
            return [d[target-n],i]
        d[n]=i
nums=[3,2,4]
target=6
print(twoSum(nums, target))