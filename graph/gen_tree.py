# 从给定的有向图生成一颗树

graph = {}

graph['a'] = ['b']
graph['b'] = ['c', 'd']
graph['c'] = ['e']
graph['d'] = []
graph['e'] = ['a']



def is_cycle(graph):
    """
    :param graph:
    :return:
    """

    for k in graph:
        stack = [k]
        visited = []

        while stack:
            current = stack.pop()

            if current in visited:
                visited.append(current)
                print(visited)
                return True
            else:
                visited.append(current)
                for k in graph[current]:
                    if graph[k]:  # 有后续结点的结点才加入栈中，成为潜在环的一结点
                        stack.append(k)
    return False

def gen_tree(graph, star_pos):
    """使用广度优先搜索可以从图中生成一棵树"""
    pass


if __name__ == "__main__":
    print(is_cycle(graph))