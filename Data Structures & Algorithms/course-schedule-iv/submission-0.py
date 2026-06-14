class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        preset = {}
        for c in range(numCourses):
            preset[c] = []

        for pre,crs in prerequisites :
            preset[crs].append(pre)

        
       

        def dfs(pre,crs,visiting):

            if pre  == crs : 
                return True

            visiting.add(crs)

            for nei in preset[crs]:
                if nei not in visiting:
                    if dfs(pre,nei,visiting):
                        return True
            return False
        

        res = []
        for pre,crs in queries : 
            if dfs(pre,crs,set()):
                res.append(True)
            else : res.append(False)

        return res





        





        
