# merge sorted arrays
def mergeSortedArrays(nums1, m, nums2, n):
    nums1[m:]=nums2
    return sorted(nums1)
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
print(mergeSortedArrays(nums1,m,nums2,n))