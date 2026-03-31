class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # 1,2,4,6  ---> 1, 2 , 8 ,48
        #              48, 48, 24,6  
       
        n = len(nums)
        precal = [1]*n
        poscal = [1]*n
        precal[0] = nums[0]
        poscal[-1] = nums[-1]
        for i in range(1,n):
            precal[i]= nums[i]* precal[i-1]

        for i in range(n-2,-1,-1):
            poscal[i] = nums[i]* poscal[i+1]

        print(precal,poscal)

        res = [1]*n
        for i in range(n):
            if i==0 : 
                left = 1
            else :  left = precal[i-1]

            if i==n-1 : 
                right = 1
            else :  right = poscal[i+1]

            res[i] = left*right

        return res

        # print(precal,poscal)