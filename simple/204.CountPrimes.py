class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        if n < 3:
            return 0
        for i in range(n):
            if self.isPrime(i):
                print i
                count += 1
        return count

    def isPrime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        num = int(n**0.5) + 1
        for i in range(2, num):
            if n % i == 0:
                return False
        return True

    def fasterCountPrimes(self, n):
        isPrime = [0] * n
        loopNum = int(n**0.5) + 1
        for i in range(2, n):
            isPrime[i] = True
        for i in range(2, loopNum):
            if not isPrime[i]:
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False
                # j += i
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count


if __name__ == '__main__':
    inputs = 10
    import datetime
    st = datetime.datetime.now()
    s = Solution()
    # print s.countPrimes(inputs)
    print s.fasterCountPrimes(inputs)
    ed = datetime.datetime.now()
    print ed
    print st
