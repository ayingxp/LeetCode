# 图的两种遍历方法，即深度优先(DFS)遍历和广度优先(BFS)遍历


# 有向图的邻接表表示 (注: 另一种表示方法为 邻接矩阵)


graph = {}

graph['a'] = ['b']
graph['b'] = ['c', 'd']
graph['c'] = ['e']
graph['d'] = []
graph['e'] = ['a']


def bfs(graph, start_pos):
    """使用队列来实现广度优先遍历"""
    queue = [start_pos]
    travel = [start_pos]

    while queue:
        current = queue.pop(0)

        if current not in travel:
            travel.append(current)

        for next_k in graph[current]:
            if next_k not in travel:
                queue.append(next_k)

    print(travel)


def dfs(graph, start_pos):
    """
    使用栈来实现深度优先遍历
    :param graph:
    :param start_pos:
    :return:
    """
    travel = []
    stack = [start_pos]

    while stack:
        current = stack.pop()
        if current not in travel:
            travel.append(current)

        for next_node in graph[current]:
            if next_node not in travel:
                stack.append(next_node)

    print(travel)


if __name__ == "__main__":
    bfs(graph, 'a')
    dfs(graph, 'a')