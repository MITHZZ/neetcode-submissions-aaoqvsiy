class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffdict = {}

        for i,n in enumerate(nums) : 
            diff = target - n

            if diff in diffdict:
                return [diffdict[diff],i]

            diffdict[n] = i

            

            
        