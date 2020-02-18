import time
import random


def bubble_sort(lst):
    for i in range(len(lst)):
        for k in range(len(lst)-1 - i):
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]


if __name__ == '__main__':
    lst = list(range(20))
    random.shuffle(lst)
    print(lst)
    bubble_sort(lst)
    print(lst)
