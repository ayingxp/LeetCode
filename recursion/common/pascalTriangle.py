"""
杨辉三角
[
    [1],
   [1,1],
  [1,2,1],
 [1,3,3,1],
[1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int):
        res = []
        for i in range(5):
            temp = []
            for j in range(i+1):
                if i == 0 or j==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(res[i-1][j-1]+res[i-1][j])
            res.append(temp)
        
        return res

    def generate_recur(self, numRows: int):
        """
        if i == 0 or j == 0 or i == j:
        f(i,j) = 1

        else:
           f(i, j) = f(i-1, j-1) + f(i-1, j)

        """

        def helper(i, j):
            if j == 0 or i==j:
                return 1
            else:
                return helper(i-1, j-1) + helper(i-1, j)

        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                tmp.append(helper(i, j))
            res.append(tmp)
        return res

        pass



if __name__ == '__main__':
    numRows = 5
    s = Solution()
    res = s.generate(numRows)
    for k in res:
        print(k)


