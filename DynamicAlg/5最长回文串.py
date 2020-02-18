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


