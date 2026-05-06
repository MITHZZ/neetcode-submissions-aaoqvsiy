class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:


        ls = len(s)
        lt = len(t)

        #lenght is same then replacement 
        #if lenght is differing by 1 then one insertion or deletion


        if ls > lt :
            return self.isOneEditDistance(t,s)


        if lt-ls > 1:
            return False

        for i in range(ls):
            if s[i] != t[i]:
                if ls == lt :
                    return s[i+1:] == t[i+1:]
                else :
                    return s[i:] == t[i+1:]

        return ls+1==lt



        