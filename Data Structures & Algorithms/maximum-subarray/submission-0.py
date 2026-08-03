class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #subarray sum 
        
        
        l = 0 
        running_sum = 0
        maxvalu = float("-inf")
        for r in range(len(nums)):
            running_sum +=nums[r]
            maxvalu = max(running_sum,maxvalu)
            if running_sum < 0:
                running_sum = 0
                l = r + 1
            
        return maxvalu