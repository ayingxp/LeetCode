# 二叉搜索树(Binary Search Tree)

from trees.btree import TreeNode, BinaryTree

class BST(BinaryTree):
    def __init__(self, root=None):
        super(BST, self).__init__(root)

    def add(self, data):  # 二叉搜索树的插入(构造)
        node = TreeNode(data)
        if not self.root:
            self.root = node
            return self.root

        else:
            current_node = self.root
            while True:
                if node.data < current_node.data:
                    # 在左子树中查找
                    if current_node.left:
                        current_node = current_node.left

                    else:
                        current_node.left = node
                        break
                else:
                    # 在右子树中查找
                    if current_node.right:
                        current_node = current_node.right

                    else:
                        current_node.right = node
                        break


if __name__ == "__main__":
    """
            A
                 K
              B   
                 F
              C     G
                 D
                    E
    """
    data = [6, 3, 7, 4, 8, 9, 10]
    bst = BST()
    for d in data:
        bst.add(d)


    print("层次遍历: ")
    bst.levelorder(bst.root)
    print("\n前序遍历: ")
    bst.preorder(bst.root)
    print("\n中序遍历: ")
    bst.inorder(bst.root)
    print("\n后续遍历: ")
    bst.postorder(bst.root)
    print("\n树的深度：")
    print(bst.deepth(bst.root))
    print("\n是否平衡: ")
    print(bst.isBalance(bst.root))