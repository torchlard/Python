Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
================================
def twoSum(nums, target):
    D = {k:v for k,v in zip( nums,range(len(nums)) ) }
    for i in range(len(nums)):
        complement = target- nums[i]
        if complement in D.keys():
            return [i, D[complement]]
    raise Exception('invalid list')

def twoSum(nums, target):
    D = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in D.keys():
            return [i, D[complement]]
        D[nums[i]] = i
    raise Exception('invalid list')

print( twoSum( [2,7,11,15] ,9 ) )

===============================


