class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        nums.reverse()

        

        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        
        for j in range(k, k + (len(nums) - k) // 2):
            nums[j], nums[len(nums)-1+k-j] = nums[len(nums)-1+k-j], nums[j]
        
        
        
        

        