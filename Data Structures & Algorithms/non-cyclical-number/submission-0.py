class Solution:
    def isHappy(self, n: int) -> bool:

        seen= set()

        tot = n
        while tot != 1 :

            digit = [int(x) for x in str(tot)]

            sumtot = 0
            for val in digit : 
                sumtot+=(val**2)

            if sumtot == 1:
                return True

            if sumtot in seen:
                return False

            seen.add(sumtot)
            tot = sumtot
            
        
        return True