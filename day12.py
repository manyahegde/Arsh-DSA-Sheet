# no. of subarrays whose sum equals k
def subarraysum(nums, k):
    prefixsum=0
    d={0:1}
    result=0
    for num in nums:
        prefixsum+=num
        if prefixsum-k in d:
            result+=d[prefixsum-k]
        if prefixsum not in d:
            d[prefixsum]=1
        else:
            d[prefixsum]+=1
    return result
print(subarraysum([1,2,-1,0,-2,2], 0))

