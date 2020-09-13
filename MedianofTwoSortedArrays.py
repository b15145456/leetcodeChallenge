num1 = [1,2]
num2 = [3,4]
#nums = [1,2,3,4] len(nums) = 4
#nums = [1,2,3] len(nums) = 3
def medianoOfTwoSortedArrays(nums1,nums2):
    nums = nums1 + nums2
    nums.sort()
    if len(nums)%2==0:
        res = (nums[int(len(nums)/2)]) + (nums[int(len(nums)/2-1)])
        res = res/2
    else:
        res = nums[int((len(nums)+1)/2-1)]
    return res
print(medianoOfTwoSortedArrays(num1,num2))
