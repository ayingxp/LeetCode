import time


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def no_recursion_cut(p, n):
    """
    递归方法,中间结果存储在 r 列表中，
    第i个元素的值表示当钢铁长度为i时，
    最优切割对应的价值

    递推式：r[k] = max(p[i] + r[k-i])
    其中，0<k<=n, 0 < i < k

    最优切割方案存放在，s列表中
    """
    r = [0]  # r 中存储计算的中间最优结果
    s = [0]

    for i in range(1, n+1):  # 求长度为 1 到 n 的钢铁的最优切割，即更新列表 r 的值
        curr_max = 0
        curr_ind = 0
        for k in range(1, i+1):
            # curr_max = max(curr_max, p[k] + r[i-k])
            if curr_max < p[k] + r[i-k]:
                curr_max = p[k] + r[i-k]
                curr_ind = k

        r.append(curr_max)
        s.append(curr_ind)
        
    
    optimals = [0]
    
    ind = n
    while True:
        optimals.append(s[n])
        n -= s[n]
        if n == 0:
            break
        
    
    return r, s, optimals


if __name__ == '__main__':
    result = no_recursion_cut(p, 9)
    print(result)
