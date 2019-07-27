# -*- coding: utf-8 -*-

"""
中心对称数：
中心对称数是指一个数字在旋转了180度之后看起来依旧相同的数字（或者上下颠倒地看）

示例：
输入: 69
输出: True


"""

class Solution:
    def isStrobogrammic(self, num):
        """

        :param num: str
        :return: bool
        """

        # 0, 1, 6, 8, 9　旋转180度以后得到新的数字，０，１，９，８，６

        if not num:
            return True
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        invalid = [2, 3, 4, 5, 7]
        N = int(num)
        n = N
        tmp = 0
        res = list()
        while n:
            n, tmp = divmod(n, 10)
            if tmp in invalid:
                return False
            res.append(mapping[tmp])

        res = res[::-1]
        r = 0
        for i, x in enumerate(res):
            r += 10**i*mapping[x]
        return r == N


if __name__ == '__main__':
    s = Solution()
    print s.isStrobogrammic('99')