class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        #so product we need to keep track of both min and max



        currentmin = nums[0]
        currentmax = nums[0]

        maxprod = nums[0]

        for num in nums[1:]:

            temp = currentmax


            currentmax = max(num, temp*num, currentmin*num)

            currentmin = min(num, temp*num, currentmin*num)


            maxprod = max(maxprod,currentmax)
        

        return maxprod