# 二叉树

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "<TreeNode: %r> " % self.data

    def __repr__(self):
        return "<TreeNode: %r>" % self.data


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        node = TreeNode(data)
        if not self.root:
            self.root = node
            return self.root

        queue = [self.root]

        while queue:
            current_node = queue.pop(0)  # 把队列头素作为当前结点
            if current_node.left:
                queue.append(current_node.left)
            else:
                current_node.left = node
                return

            if current_node.right:
                queue.append(current_node.right)
            else:
                current_node.right = node
                return

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def levelorder(self, root):
        if not root:
            return
        queue = [root]
        results = []

        while queue:
            current_node = queue.pop(0)
            results.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        for i in results:
            print(i, end=" ")


    def isBalance(self, root):
        """判断树是否平衡"""
        if not root:
            return True

        else:
            left_deep = self.deepth(root.left)
            right_deep = self.deepth(root.right)

            if abs(left_deep - right_deep) <= 1:
                return True
        return False

    def deepth(self, root):
        """判断树的深度"""
        deep = 0
        if not root:
            return deep
        else:
            left_deep = self.deepth(root.left)
            right_deep = self.deepth(root.right)
        return max(left_deep, right_deep) + 1


if __name__ == "__main__":
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    g = TreeNode("G")

    data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    btree = BinaryTree()
    for d in data:
        btree.add(d)

    print("前序遍历: ")
    btree.preorder(btree.root)
    print("\n中序遍历: ")
    btree.inorder(btree.root)
    print("\n后续遍历: ")
    btree.postorder(btree.root)
    print("\n层次遍历: ")
    btree.levelorder(btree.root)

    print("\n树的深度: ")
    print(btree.deepth(btree.root))

    print("\n判断树是否平衡: ")
    print(btree.isBalance(btree.root))



    # print(a, b, c, d, e, f)