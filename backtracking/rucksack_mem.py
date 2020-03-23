# 使用记忆化搜索求解 0-1 背包问题

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

def search_mem(depth, pack_limit):
    if depth == len(info) - 1:
        return info[depth][1] if pack_limit >= info[depth][0] else 0

    else:
        # 分任务
        # 选择不放 info[depth] 元素
        not_put_value = search_mem(depth + 1, pack_limit)

        # 选择放 info[depth] 元素
        if pack_limit >= info[depth][0]:
            put_value = search_mem(depth + 1, pack_limit - info[depth][0]) + info[depth][1]
        else:
            put_value = not_put_value

        return max(not_put_value, put_value)  # 选最优策略


if __name__ == "__main__":
    pack_limit = 5
    depth = 0

    res = search_mem(depth, pack_limit)
    print(res)