class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        count = {}

        maxheap = []
        for num in nums :
            count[num] = 1 + count.get(num,0)
        
        for key, value in count.items():
            heapq.heappush(maxheap,(value*-1,key))

        res = []
        i = 1
        while i <= k:
            key,num = heapq.heappop(maxheap)
            res.append(num)
            print(num)
            i+=1

        return res

        # while maxheap:
        #     print(heapq.heappop(maxheap))


        # print(heapq)
        