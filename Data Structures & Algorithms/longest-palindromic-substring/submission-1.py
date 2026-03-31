class Solution:
    def longestPalindrome(self, s: str) -> str:

        resIdx, resLen = 0, 0
        n = len(s)

        rows = n
        cols = n

        dp = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(n):
            dp[i][i] = 1
            resIdx, resLen = i, 1

        for length in range(2,rows+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > resLen:
                            resIdx, resLen = i, length

        return  s[resIdx:resIdx + resLen]