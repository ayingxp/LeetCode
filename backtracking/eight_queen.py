"""
八皇后问题
"""

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


def is_conflict(board, x, y):
    # 判断相同行有没有冲突
    for i in range(y):
        if board[x][i] == 1:
            print("同行")
            return True
    # 判断相同列有没有冲突
    for i in range(x):
        if board[i][y] == 1:
            print("同列")
            return True

    # 判断对角线有没有冲突
    for i in range(x):
        for j in range(y+1, len(board)):
            if (j-y) / (i-x) == -1.0 and board[i][j] == 1:
                print("对角线")
                return True

    # 判断反对角线有没有冲突
    for i in range(x):
        for j in range(y):
            if (j-y) / (i-x) == 1.0 and board[i][j] == 1:
                print("反对角线")
                return True

    return False


def put_queen(board):
    stack_path = []
    for i in range(len(board)):
        for j in range(len(board)):
            if is_conflict(board, i, j):
                continue
            else:
                board[i][j] = 1
                stack_path.append((i, j))
                break
        else:
            x, y = stack_path.pop()
            board[x][y] = 0


res = []

def put_queen_rec(board, step):
    if step == len(board):
        res.append(board[:])
        return
    else:
        for i in range(len(board)):
            if not is_conflict(board, step, i):
                board[step][i] = 1
                put_queen_rec(board, step + 1)
                board[step][i] = 0


def can_place(x, y):
    """
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    :param x:
    :param y:
    :return:
    """
    # 判断x行
    for i in range(y):
        if board[x][i] == 1:
            return False

    # 判断y列
    for i in range(x):
        if board[i][y] == 1:
            return False

    # 判断对角线
    for i in range(x):
        if x + y - i <= 7:    #   对角线: (i, j) 和 (x, y)两点, 满足 i+j = x + y
            if board[i][x+y-i] == 1:
                return False

    # 判断反对角线
    for index, i in enumerate(range(x-1, -1, -1)):
        s_y = y - (index + 1)   #  反对角线上两点: (i, j) 和 (x, y)两点满足
        if s_y >= 0:
            if board[i][s_y] == 1:
                return False

    return True




def put_queen_rec2(step):
    if step == len(board):
        # res.append(board[:])
        pprint(board)
        # return
    else:
        for i in range(len(board)):
            if can_place(step, i):
                board[step][i] = 1
                put_queen_rec2(step+1)
                board[step][i] = 0

if __name__ == "__main__":
    from pprint import pprint
    # put_queen(board)
    # put_queen_rec(board, 0)
    put_queen_rec2(0)
    # pprint(board)
    # pprint(res)
