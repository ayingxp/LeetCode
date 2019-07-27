# -*- coding: utf-8 -*-

"""
给定一棵二叉树，找到最长的路径，这个路径中的每个节点具有相同值。
这条路径可以经过也可以不经过根节点。

注：两个节点之间的路径长度由它们之间的边数表示。

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, root, val):
        if not root:
            return 0
        lmax, lvalue = self.dfs(root.left, root.val)
        rmax, rvalue = self.dfs(root.right, root.val)

        nowMax = max(lmax, rmax, lvalue + rvalue)

        if root.val != val:
            return nowMax, 0
        nowValue = max(lvalue, rvalue) + 1
        return nowMax, nowValue


    def longestUnivaluePath(self, root):
        """

        :param root: TreeNode
        :return: int
        """
        if root == None:
            return 0
        return self.dfs(root, root.val)[0]


if __name__ == '__main__':
    data = [5, 4, 5, 1, 1, 5]
