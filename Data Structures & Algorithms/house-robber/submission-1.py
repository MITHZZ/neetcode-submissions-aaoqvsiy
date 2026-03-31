class Solution:
    def rob(self, nums: List[int]) -> int:


        # 1,1,3,3

        #  0,0,1

        pp,p = 0,0
        res = [0]*len(nums)
        for i in range(len(nums)):
            amount = max(pp+nums[i],p)
            res[i] = amount
            pp = p
            p = amount

        return res[len(nums)-1]
