import time


def get_longest_common_subsequence(a, b):
    """
    dp[i][j]定义a[0]-a[i] 和 b[0]-b[j]的最长子序列长度
    """
    dp = [[0] * (len(b)+1) for _ in range(len(a) + 1)]
    for k in dp:
        print(k)

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        for k in dp:
            print(k)
        print('**'*30)

    return dp[len(a)][len(b)]

if __name__ == '__main__':
    print('Hello World!')
    a = 'abcbdab'
    b = 'bdcaba'
    dp = get_longest_common_subsequence(a, b)
    print(dp)
