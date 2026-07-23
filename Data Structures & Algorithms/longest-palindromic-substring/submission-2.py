class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i]=1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                start = i
                max_len = 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1] > 0:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    if dp[i][j] > max_len:
                        start = i
                        max_len = dp[i][j]

        return s[start:start + max_len]