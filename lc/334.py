class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        max_num = [0] * n
        max_num[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            max_num[i] = max(nums[i], max_num[i+1])
        
    
        min_num = nums[0]
        for i in range(1, len(nums)):
            if min_num < nums[i] < max_num[i]:
                return True
            min_num = min(min_num, nums[i])

        return False