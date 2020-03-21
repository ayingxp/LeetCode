
from trees.alex.bitree import BiTreeNode

class TreeNode(BiTreeNode):
    def __init__(self, data):
        super(TreeNode, self).__init__(data)
        self.parent = None


class BST:
    def __init__(self):
        self.root = None


    def insert(self, node, data):
        if not node:
            node = TreeNode(data)

        elif data < node.data:
            node.lchild = self.insert(node.lchild, data)
            # node.lchild.parent = node

        elif data > node.data:
            node.rchild = self.insert(node.rchild, data)
            # node.rchild.parent = node

        return node

    def insert_no_recu(self, data):
        current_node = self.root

        if not current_node:
            self.root = TreeNode(data)
            return

        while True:
            if data < current_node.data:
                if current_node.lchild:
                    current_node = current_node.lchild

                else:  # 左孩子不存在
                    current_node.lchild = TreeNode(data)
                    current_node.lchild.parent = current_node
                    return

            elif data > current_node.data:
                if current_node.rchild:
                    current_node = current_node.rchild

                else:
                    current_node.rchild = TreeNode(data)
                    current_node.rchild.parent = current_node
                    return

            else:
                return

    def inorder(self, root):
        if root:
            self.inorder(root.lchild)
            print(root.data, end=",")
            self.inorder(root.rchild)


    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

if __name__ == "__main__":
    """
            E
           / \
          A   G
           \  /
           C  F
          / \
         B   D
    """

    items = list("EAGCFBD")
    tree = BST()

    for data in items:
        tree.root = tree.insert(tree.root, data)
        print(tree.root)
        # tree.insert_no_recu(data)

    tree.inorder(tree.root)
    print()
    tree.pre_order(tree.root)

