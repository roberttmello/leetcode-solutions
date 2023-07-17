
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j] 
    return    
    
nums_1 = [2,7,11,15]
target_1 = 9
print(twoSum(nums_1,target_1))

nums_2 = [3,2,4]
target_2 = 6
print(twoSum(nums_2,target_2))

nums_3 = [3,3]
target_3 = 6
print(twoSum(nums_3,target_3))

nums_4 = [2,5,5,11]
target_4 = 10
print(twoSum(nums_4, target_4))
