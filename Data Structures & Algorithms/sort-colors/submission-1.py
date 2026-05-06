class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq = {}

        for c in nums:
            freq[c] = freq.get(c,0)+1

        colors = [0,1,2]

        i=0
        for color in colors:
            count = freq.get(color, 0)
            lastindex = i
            while i<count+lastindex:
                nums[i] = color
                i+=1
