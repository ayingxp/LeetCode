"""
以相反的顺序打印字符串
"""

def print_reverse(my_str):
    if len(my_str) == 0:
        return
    print_reverse(my_str[1:])
    print(my_str, my_str[0])


def print_reverse_2(my_str):
    if len(my_str) <= 1:
        return
    else:
        my_str[0], my_str[-1] = my_str[-1], my_str[0]
        print_reverse_2(my_str[1:-1])


def reverse_String(s):
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)
    helper(0, len(s) - 1)

if __name__ == "__main__":
    my_string = list('abcdefg')
    print(my_string)
    # print_reverse(my_string)
    reverse_String(my_string)
    print('res:\n', my_string)
