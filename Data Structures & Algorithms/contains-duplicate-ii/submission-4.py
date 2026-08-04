class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l = 0
        
        for r in range (1,len(nums)):

            while not abs(l-r) <= k:
                l+=1
            
            for i in range(l, r):
                if nums[r] == nums[i] :
                    return True
            

            

        return False
