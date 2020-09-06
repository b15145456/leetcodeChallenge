nums = [1,6,12,7]
target = 7

def twoSumFunc1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSumFunc2(nums, target):
        seen = {}
        for index, num in enumerate(nums):
            other = target - num
            print(other)
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
        return []
        
a = twoSumFunc2(nums, target)
print(a)
