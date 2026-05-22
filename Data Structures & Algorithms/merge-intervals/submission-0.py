class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:



        # [1,3],[2,5],[6,7]



        # 1 2 3
        #   2 3 4 5 
        #           6 7 

        # 1,2
        #   2 3  

        res = []
        intervals.sort(key=lambda x:x[0])
        if not intervals: return []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            prevs,preve = res[-1]

            if start <= preve:
                res[-1] = [prevs, max(preve, end)]
            else :

                res.append([start,end])
        return res
        print(res)