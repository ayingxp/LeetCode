# 使用动态规划(自底向上)算法实现 0-1 背包问题

"""
===== ===== ===== =====
重量    3     2     5
====  ===== ===== =====
价值    8     5     12
====  ===== ===== =====
"""

from pprint import pprint

info = [
    [3, 8],
    [2, 5],
    [5, 12]
]
capacity = 5


# dp[i][j] 表示 第i个物品在背包容量为 j 时的最优价值

dp = [[0 for i in range(capacity + 1)] for _ in range(len(info))]

# pprint(bp)


def search_dp(info):
    # if depth == len(info):
    #     pass
    for i in range(1, len(info) + 1):
        for j in range(1, capacity + 1):
            if info[i][0] > j:   #  如果背包的剩余空间(质量)不够, 则采用
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-info[i][0]] + info[i][1])

def search_dp(info, c):
    # dp[i][j] 表示 第i个物品在背包容量为 j 时的最优价值
    # 顺序选择
    for i in range(len(info)):
        for j in range(1, c + 1):
            if j < info[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                # f(i, j) = max [f(i-1, j), f(i-1, j - w[i]) + v[i]
                # f(i-1, j) 表示 全部 j 单位的背包容量给前 (i - 1) 个物品， 即 不选 第i个物品
                # f(i-1, j - w[i]) + v[i] 表示 选择 第 i 个物品， 前 i - 1 个物品占用 j - w[i] 单位的背包容量
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - info[i][0]] + info[i][1])
    print(dp[-1][-1])


if __name__ == "__main__":
    search_dp(info, capacity)
    print(dp)


