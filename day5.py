# move zeroes
def moveZeroes(nums):
    ind=0
    for i in range(0, len(nums)):
        if nums[i]!=0:
            nums[ind]=nums[i]
            ind+=1
    nums[ind:]=[0]*(len(nums)-ind)
nums=[0,1,0,3,12]
moveZeroes(nums)
print(nums)