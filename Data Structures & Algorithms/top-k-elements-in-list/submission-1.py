class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        

        maxheap = []

        for num, freq in freq.items():
            heapq.heappush(maxheap,(freq*-1,num))
        
        i = 1
        res = []
        while i<=k:
            freq,num = heapq.heappop(maxheap)
            res.append(num)
            i+=1

        return res

