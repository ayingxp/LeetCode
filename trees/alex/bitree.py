class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return "<BiTreeNode %r>" % self.data

    def __repr__(self):
        return "<BiTreeNode %r>" % self.data

def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)

def pre_order_no_rec(root):
    """使用栈来实现非递归遍历"""
    stack = []
    result = []

    current_node = root

    while current_node or stack:
        while current_node:
            stack.append(current_node)
            result.append(current_node.data)
            current_node = current_node.lchild

        if stack:
            current_node = stack.pop()
            current_node = current_node.rchild
    print(result)



def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

def in_order_no_rec(root):
    stack = []
    result = []
    current_node = root

    while current_node or stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.lchild

        if stack:
            current_node = stack.pop()
            result.append(current_node.data)
            # 进入右子树
            current_node = current_node.rchild

    print(result)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


def post_order_no_recu(root):
    if not root:
        return None

    stack = []
    current_node = root
    last_node = None
    result = []

    # 遍历到左子树最下边的叶子结点，并保存遍历过程中的结点
    while current_node:
        stack.append(current_node)
        current_node = current_node.lchild

    while stack:
        current_node = stack.pop()
        if not current_node.rchild or current_node.rchild == last_node:
            result.append(current_node.data)
            last_node = current_node

        else:
            stack.append(current_node)
            current_node = current_node.rchild

            while current_node:
                stack.append(current_node)
                current_node = current_node.lchild

    print(result)



def level_order(root):
    """使用队列来实现层次遍历"""
    queue = [root]
    result = []
    while queue:
        current_node = queue.pop(0)
        if current_node:
            result.append(current_node.data)

        if current_node.lchild:
            queue.append(current_node.lchild)

        if current_node.rchild:
            queue.append(current_node.rchild)

    print(result)



if __name__ == "__main__":
    """
            E
           / \
          A   G
           \   \
           C    F
          / \
         B   D
    """

    a = BiTreeNode("A")
    b = BiTreeNode("B")
    c = BiTreeNode("C")
    d = BiTreeNode("D")
    e = BiTreeNode("E")
    f = BiTreeNode("F")
    g = BiTreeNode("G")

    e.lchild = a
    e.rchild = g
    a.rchild = c
    c.lchild = b
    c.rchild = d
    g.rchild = f

    root = e

    print(root.lchild.data)
    print(root.rchild.data)

    print("前序遍历: ")
    pre_order(root)
    print()
    pre_order_no_rec(root)
    print("\n中序遍历: ")
    in_order(e)
    print()
    in_order_no_rec(root)
    print("\n后续遍历: ")
    post_order(e)
    print()
    post_order_no_recu(e)

    print("\n层次遍历: ")
    level_order(root)

