"""
    回文串：
        正读和反读都一样的字符串，比如“level”和“noon”等就是回文串。[百度百科]
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        pass

    def slow_method(self, s: str) -> str:
        if len(s) < 2:
            return s

        res = []
        curr_res = ''
        for i in range(2, len(s) + 1):
            for k in range(i, len(s) + 1):
                subStr = s[k-i:k]
                if self.isPalindrome(subStr):
                    res.append(subStr)
                    curr_res = subStr
    
    def isPalindrome(s):
        if len(s) < 2:
            return True
        elif len(s) % 2 == 0:
            if s[:len(s)//2] == s[len(s)//2:][::-1]:
                return True
        elif len(s) % 2 == 1:
            if s[:len(s)//2] == s[len(s)//2 + 1:][::-1]:
                return True
        return False


def longestPalindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    max_len = 1
    start = 0
    
    for i in range(n):
        dp[i][i] = True
        if i<n-1 and s[i]==s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2

    for l in range(3, n+1):
        for i in range(n+1-l):
            r = i + l - 1
            if s[i] == s[r] and dp[i+1][r-1]:
                dp[i][r] = True
                start = i
                max_len = l
    
    return s[start:start+max_len]
    

if __name__ == '__main__':
    tstr = 'noon'
    substr = longestPalindrome(tstr)
    print(substr)
