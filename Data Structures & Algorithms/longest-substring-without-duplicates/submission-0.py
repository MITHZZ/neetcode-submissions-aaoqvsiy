class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visit = set()

        l= 0
        r = l

        res = 0

        while  r < len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l+=1
            
            visit.add(s[r])
            length = r-l+1
            res = max(res,length)
            r+=1
        
        return res



        

        