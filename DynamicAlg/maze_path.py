from pprint import pprint

dirs = [
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x, y + 1),  # 右
]


def maze_stack(maze, start, end):
    """
    maze: 迷宫矩阵
    start: 起始位置
    end: 目标位置
    """

    stack = []
    stack.append(start)

    while len(stack) > 0:
        curNode = stack[-1]  # 当前位置的坐标
        # print(stack)
        # pprint(maze)
        if curNode == end:
            print("The path is:\n")
            print(stack)
            return True
        # 往四个方向移动
        # 使用　for else语句, for　正常执行完成，则else也会正常执行
        # for 提前退出时, else　不会执行
        for _dir in dirs:
            nextNode = _dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # 当前点可走时，将其放在stack里面
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    # else:
    print("No path")
    pprint(maze)
    return False

if __name__ == '__main__':
    maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    maze_stack(maze, (1, 1), (5, 5))
