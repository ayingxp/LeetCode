# 0-1 背包问题


# 1. 通过回溯法求解 0-1 背包问题

"""
===== ===== ===== =====
重量    3     2     5
====  ===== ===== =====
价值    8     5     12
====  ===== ===== =====
"""

info = [
    [3, 8],
    [2, 5],
    [5, 12]
]

results = []
max_selects1 = [0 for _ in range(len(info))]

def search(depth, pack_limit):
    """

    :param pack_limit: 剩余背包容量
    :param depth: 搜索的深度
    :return:
    """
    if depth >= len(info): # or pack_limit < min([item[0] for item in info[depth:]]):
        print(results)
        global max_selects1
        if sum(results) > sum(max_selects1):
            max_selects1 = results[:]

    else:
        results.append(0)  # 试探步骤(设置现场), 表示不选择info[depth]元素，即xi 设置为0
        search(depth + 1, pack_limit)  # 进一步搜索, 即 往depth增加的方向(depth + 1)
        results.pop()  # 回溯步骤(恢复现场)

        if pack_limit >= info[depth][0]:
            results.append(1)  # 试探， 即选择info[depth], 也即xi 设置为1
            search(depth+1, pack_limit - info[depth][0])
            results.pop()


selects = []
max_selects = [0, 0, 0]

def search2(depth, pack_limit):
    """

    :param pack_limit: 剩余背包容量
    :param depth: 搜索的深度
    :return:
    """

    if depth == len(info):
        print(selects)
        global max_selects
        if sum(selects) > sum(max_selects):
            max_selects = selects[:]
            print("Current max selects: ", max_selects)


    else:
        selects.append(0)  # 试探步骤(设置现场), 表示不选择info[depth]元素，即xi 设置为0
        search2(depth + 1, pack_limit)  # 进一步搜索, 即 往depth增加的方向(depth + 1)
        selects.pop()  # 回溯步骤(恢复现场)

        if pack_limit >= info[depth][0]:
            selects.append(1)  # 试探， 即选择info[depth], 也即xi 设置为1
            search2(depth+1, pack_limit - info[depth][0])
            selects.pop()


if __name__ == "__main__":
    pack_limit = 5

    # search(0, pack_limit)
    search(0, pack_limit)
    print("***"*20)
    # print(max_selects)
    print(max_selects1)