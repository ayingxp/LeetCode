class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(n+1):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    inputs = 10
    s = Solution()
    print s.countPrimes(inputs)
