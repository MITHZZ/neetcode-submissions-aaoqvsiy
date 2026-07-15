from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        adj = defaultdict(list)
        for src,des,time in times : 
            adj[src].append((time,des))

        minheap = [(0,k)]

        visited = set()

        res = 0

        while minheap : 
            time,des =  heapq.heappop(minheap)
            if des in visited:
                continue
            visited.add(des)
            t = time
            for time2,nei in adj[des]:
                if nei not in visited:
                    heapq.heappush(minheap,(time+time2,nei))
        return t if len(visited) == n else -1
        
        



