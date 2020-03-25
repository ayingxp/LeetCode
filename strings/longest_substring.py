"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from pprint import pprint

string = "abcabcbb"
string = "bbbbb"
string = "pwwkew"

dp = [[0 for _ in range(len(string))] for _ in range(len(string))]

# pprint(dp)

def longestSubstringNoRepeat2(string):
    result = {}
    index, length = 0, 0

    for i in range(len(string)):
        if string[i] in result:
            index = max(result[string[i]], index)
        length = max(length, i - index + 1)
        result[string[i]] = i + 1

    return length


l = longestSubstringNoRepeat2(string)
print(l)
exit()

def longestSubstringNoRepeat(string):
    """
    f(i, j)  =  1,  if i == j (i<=j)
    f(i, j) = f(i, j-1) + 1 , if s[j] not in s[i...j-1]
    f(i, j) = f(i, j-1) , if s[j] in s[i...j-1]

    :param string:
    :return:
    """
    #
    # for i in range(len(string)):
    #     dp[i][i] = 1

    for i in range(len(string)):
        for j in range(i, len(string)):
            if i == j:
                dp[i][j] = 1
            else:
                if string[j] not in string[i:j]:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    break


if __name__ == "__main__":
    longestSubstringNoRepeat(string)
    max_length = 0
    for row in dp:
        for col in row:
            if col > max_length:
                max_length = col


    pprint(dp)
    print(max_length)

