def bin_search_no_rec(lst, value):
    if not lst:
        return None
    if value < lst[0] or value > lst[-1]:
        return None

    low = 0
    high = len(lst) - 1
    mid = (low + high) // 2

    while low <= high:
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            high = mid - 1
        elif lst[mid] < value:
            low = mid + 1
        mid = (low + high) // 2

    return None

def bin_search_rec(lst, value, low, high):
    if low > high:
        return None
    mid = (low + high) // 2

    if lst[mid] == value:
        return mid

    else:
        if lst[mid] < value:
            low = mid + 1
            res = bin_search_rec(lst, value, low, high)
        else:
            high = mid - 1
            res = bin_search_rec(lst, value, low, high)

    return res






if __name__ == "__main__":
    data = [1, 7, 17, 18, 27, 29, 30, 35, 39, 41, 66, 67, 78, 82, 91, 92]

    # ind = bin_search_no_rec(data, 2)
    ind = bin_search_rec(data, 18, 0, len(data)-1)
    print(ind)
    if ind:
        print(data[ind])