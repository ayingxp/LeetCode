"""
以相反的顺序打印字符串
"""

def print_reverse(my_str):
    if len(my_str) == 0:
        return
    print_reverse(my_str[1:])
    print(my_str, my_str[0])

if __name__ == "__main__":
    my_string = 'abcdefg'
    print_reverse(my_string)
