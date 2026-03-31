class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # XYYXDDXX -  this is the string 

        # x ---> y--> y--> x longest = 4 , if x == D no YYXD , YXDD - YYYYXX,XDDXX 

        # ii

        # aaababb : a a a a a = 5


        # x : 2
        # y : 2

        # 4 - x = 2 > 3
        # k = 2

        valid = {}
        res = 0
        l = 0

        for r in range(0,len(s)):
            valid[s[r]] = valid.get(s[r],0)+1

            if (r-l+1) - max(valid.values()) > k:
                valid[s[l]]-=1
                l+=1
            else :
                res = max(res,r-l+1)        
        return res 
