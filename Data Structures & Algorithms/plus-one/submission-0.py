class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        r = len(digits)-1

        carry = 1
        while r >= 0:

            newval = digits[r] + carry
            digits[r] = newval % 10
            carry = newval // 10

            r-=1

        if carry !=0:
            digits = [carry] + digits

        return digits


        