class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxval = float("-inf")

        # order of n square
        for l in range(0,len(heights)-1):
            for r in range(1,len(heights)):
                area = (r-l) * min(heights[l],heights[r])
                maxval = max(maxval,area)

        # l = 0
        # for 

        return maxval
                