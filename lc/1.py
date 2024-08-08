class Solution(object):
    def twoSum(self, nums, target):
        numList = {}

        for i in range(len(nums)):
            if target-nums[i] in numList:
                return [numList[target-nums[i]], i]
            numList[nums[i]] = i
            
