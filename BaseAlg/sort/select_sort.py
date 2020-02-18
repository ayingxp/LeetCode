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


def select_sort_2(lst):
    min_index = 0

    for ind in range(len(lst)):
        for k in range(ind, len(lst)):
            if lst[ind] > lst[k]:
                lst[ind], lst[k] = lst[k], lst[ind]

    return lst


if __name__ == '__main__':
    lst = list(range(20))
    random.shuffle(lst)

    print(lst)
    #res = select_sort_1(lst)
    res = select_sort_2(lst)
    print(res)

