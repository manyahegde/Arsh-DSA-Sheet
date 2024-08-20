# Subarray Sums Divisible by K
def subArrDivByK(nums, k):
    d={0:1}
    prefsum=0
    count=0
    for num in nums:
        prefsum+=num
        mod=prefsum%k
        if mod<0:
            mod+=k
        if mod in d:
            count+=d[mod]
            d[mod]+=1
        else:
            d[mod]=1
    return count
nums=[4,5,0,-2,-3,1]
k=5
print(subArrDivByK(nums, k))