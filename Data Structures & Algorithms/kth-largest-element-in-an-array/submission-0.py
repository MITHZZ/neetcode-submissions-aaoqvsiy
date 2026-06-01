class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # array of numbers 
        # integer k 
        # kth largest element in array 



        minheap = []

        for n in nums:
            heapq.heappush(minheap,-1*n)

        res= -1
        while k > 0: 
            res = heapq.heappop(minheap)*-1
            k-=1

        
        return res
        