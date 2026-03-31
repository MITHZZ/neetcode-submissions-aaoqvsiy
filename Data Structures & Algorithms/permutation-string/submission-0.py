class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        l = 0
        
        verify = {}
        for c in s1:
            if c in verify : 
                verify[c]+=1
            else : verify[c] = 1

        for r in range(1,len(s2)+1):
            if r - l > len(s1):
                l+=1
            current = s2[l:r]
            temp = {}
            for c in current : 
                if c in temp : 
                    temp[c]+=1
                else : 
                    temp[c] = 1
            if temp == verify:
                return True

        return False


