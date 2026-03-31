class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float("inf")


        l = 0
        r = 0
        tot = 0

        while r < len(nums):
            tot += nums[r]
            while tot >= target :
                res = min(res,r-l+1)
                tot-=nums[l]
                l+=1
            r+=1

        return res if res != float("inf") else 0

        

        