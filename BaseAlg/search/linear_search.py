def linear_search(lst, target):
    for k, v in enumerate(lst):
        if v == target:
            return lst.index(v)
    return False


if __name__ == '__main__':
    a = list(range(10000))

    import time
    s = time.time()

    ind = linear_search(a, 8999)

    print(ind)

    e = time.time()

    print(e-s)
