class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        frecheck = {}

        for v in s : 
            frecheck[v] = frecheck.get(v,0) + 1
        
        for v in t : 
            if v not in frecheck:
                return False
            frecheck[v]-=1

        for val in frecheck.values():
            if val > 0:
                return False
        return True
            
        