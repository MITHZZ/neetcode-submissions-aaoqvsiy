class Solution:
    def isPalindrome(self, s: str) -> bool:

        print(s)
        print(s[::-1])

        newstring = []
        for c in s : 
            if c.isalnum():
                newstring.append(c.lower())
        sn = "".join(newstring)
        reversstrin = sn[::-1]
        return sn == sn[::-1]
        