class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
          

        prereq = {}
        for crs in range(numCourses):
            prereq[crs] = []

        for crs ,pre in prerequisites: 
            prereq[crs].append(pre)

        #there two varaible needed path and another is visited (if true cycle)
        visiting =set()
        visited = set()
        res = []
        def dfs(crs):
            if crs in visiting : 
                return False
            if crs in visited:
                return True

            visiting.add(crs)

            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)

            return True



        for crs in range(numCourses) : 
            if not dfs(crs):
                return []

        return res