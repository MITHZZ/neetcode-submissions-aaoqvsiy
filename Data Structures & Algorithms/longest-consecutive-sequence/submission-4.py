class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        # if length zero then zero
        # if lenght 1 is then one

        # if great then one 

        # if each element check its next element is present then continue..until con break


        # length = len(nums)
        # if length <= 1:
        #     return length

        # res = 0

        # check = set(nums)

        # i = 0
        # while i < length:
        #     current = 0
        #     cur_vl = nums[i]+1 
        #     while  cur_vl in check:
        #         current+=1
        #         cur_vl+=1
        #     res= max(current,res) 
        #     i+=1
        # return res+1

        # length = len(nums)
        # if length <=1:
        #     return length
        
        # check = set(nums)
        # maxlenght = 1
        # for num in nums:
        #     count = 1
        #     newnum = num+1
        #     while newnum  in check :
        #         count+=1
        #         newnum+=1
        #         maxlenght = max(maxlenght,count)

        # return maxlenght













        # make the set
        setm = set(nums)

        longest = 0
        for i in range(len(nums)):
            res = 1
            nextval = nums[i]+1
            while nextval in setm:
                res+=1
                nextval+=1
            longest = max(longest,res)
        
        return longest









        
            

            
            
        