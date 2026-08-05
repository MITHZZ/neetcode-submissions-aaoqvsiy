class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        


        # ciruclar array 

        # [[array]......[array]] - warapping

        # in order ro maximu sum in wrappin we need to have min sum in the middle



        # maxsum = total-minsum


        # bestinsubbray = max(maxsubarway, total-minsum)

        currentmax = nums[0]
        currentmin = nums[0]

        bestmin = nums[0]
        bestmax = nums[0]

        total = nums[0]

        for num in nums[1:]:
            currentmax = max(num,currentmax+num)
            bestmax = max(bestmax,currentmax)
            currentmin = min(num,currentmin+num)
            bestmin = min(bestmin,currentmin)

            total+=num

        
        if bestmax<0:
            return bestmax

        return max(bestmax,total-bestmin)

            




