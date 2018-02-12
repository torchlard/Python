def twoSum(nums, target):
    D = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in D.keys():
            return [i, D[complement]]
        D[nums[i]] = i
    raise Exception('invalid list')

print( twoSum( [2,6,11,7] ,9 ) )




