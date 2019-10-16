#  -*- coding: utf-8 -*-

def minWindow(s, t):
    import collections

    d = collections.Counter(t)
    res_len = float('inf')

    head = 0
    seats = len(t)
    start = 0

    for tail, char in enumerate(s):
        d[char] = d.get(char, 0) - 1
        if d[char] >= 0:
            seats -= 1
        while seats == 0:
            if tail - head + 1 < res_len:
                start = head
                res_len = tail - head + 1
            ch = s[head]
            d[ch] += 1
            if d[ch] > 0:
                seats += 1
            head += 1
    if res_len != float('inf'):
        return s[start:start + res_len]
    return ""


if __name__ == '__main__':
    s = 'addbecodebanc'
    t = 'abc'

    result = minWindow(s, t)
    print result
