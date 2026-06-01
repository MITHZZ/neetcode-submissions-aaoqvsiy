class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        # we can sit idle 
        # we need to have  atleant n cpu culetes to complete




        alphabetvalue = {}
        minheap = []

        for task in tasks:
            alphabetvalue[task] = alphabetvalue.get(task,0) + 1

        for key,value in alphabetvalue.items():
            heapq.heappush(minheap,-1*value)

        time = 0
        q  = deque()
        while minheap or q :
            time += 1
            if minheap:
                cnt = 1+heapq.heappop(minheap)
                if cnt : 
                    q.append([cnt,time+n])

            if q and q[0][1] == time:
                heapq.heappush(minheap,q.popleft()[0])

        return time







        
        