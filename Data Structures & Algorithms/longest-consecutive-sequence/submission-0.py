class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        # if length zero then zero
        # if lenght 1 is then one

        # if great then one 

        # if each element check its next element is present then continue..until con break


        length = len(nums)
        if length <= 1:
            return length

        res = 0

        check = set(nums)

        i = 0
        while i < length:
            current = 0
            cur_vl = nums[i]+1 
            while  cur_vl in check:
                current+=1
                cur_vl+=1
            res= max(current,res) 
            i+=1

        return res+1
            

            
            
        