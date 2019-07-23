class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            k = int((2*n)**0.5)
            if k*(k+1) <= 2*n:
                return k
            else:
                return k - 1


if __name__ == '__main__':
    inputs = range(100)
    s = Solution()
    for i in inputs:
        print i, s.arrangeCoins(i)
