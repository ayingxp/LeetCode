import time
import random
import sys


def select_sort_1(lst):

    res = []
    for i, v in enumerate(lst):
        if i == 0:
            res.append(v)
        else:
            if res[-1] <= v:
                res.append(v)
            else:
                for k in range(len(res)):
                    if res[k] >= v:
                        res.insert(k, v)
                        break
    return res


if __name__ == '__main__':
    lst = list(range(20))
    random.shuffle(lst)

    print(lst)
    res = select_sort_1(lst)
    print(res)

