class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def getDeepth(self, root):
        if root is None:
            return 0

        right_length = self.getDeepth(root.right)
        left_length = self.getDeepth(root.left)
        return max(right_length, left_length) + 1


    def isBalance(self, root):
        if Root is None:
            return True
        
        right = self.getDeepth(root.right)
        left = self.getDeepth(root.left)

        if abs(right - left) > 1:
            return False
        return self.isBalance(root.right) and isBalance(root.left)

