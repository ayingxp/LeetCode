"""
回溯算法之 全排列

输入: [1,2,3]
输出: [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """

        :param nums: List[int]
        :return: List[List[int]]
        """
        output = []
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])  # nums[:] will make deep copying
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()

        return output


if __name__ == '__main__':

    import pprint

    nums = [1, 2, 3]

    s = Solution()

    output = s.permute(nums)

    pprint.pprint(output)
