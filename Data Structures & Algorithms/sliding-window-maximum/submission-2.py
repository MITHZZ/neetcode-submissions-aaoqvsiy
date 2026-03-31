class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # 1,2,1,0,4,2,6

        # res = []

        # l = 0

        # count = 0
        # maxval = float('-inf')
        # for r in range(len(nums)):
        #     count+=1
        #     maxval = max(maxval,nums[r])
        #     if count == k :
        #         res.append(maxval)

        #     if count > k:
        #         l+=1
        #         maxval = max(nums[l:r+1])
        #         res.append(maxval)
        #         count -=1
            
            
        # return res


        res = []

        q = deque()


        r = 0
        l = 0
        while r < len(nums):
            #when new values come we need to pop all the values less it in queue
            while q and q[-1] < nums[r]:
                q.pop()
            
            #if all the less values are popped then append the new value
            q.append(nums[r])

            if r-l+1 == k :
                res.append(q[0])
                if q[0] == nums[l]:
                    q.popleft()
                l+=1
            r+=1

        return res
            



            

        

