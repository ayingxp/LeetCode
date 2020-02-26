"""
归并排序
"""

def merge(lst, low, mid, high):
    i = low
    j = mid + 1

    res = []

    while i <= mid and j <= high:
        if lst[i] <= lst[j]:
            res.append(lst[i])
            i += 1
        else:
            res.append(lst[j])
            j += 1

    while i <= mid:
        res.append(lst[i])
        i += 1

    while j <= high:
        res.append(lst[j])
        j += 1

    lst[low:high+1] = res



def merge_sort(lst, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(lst, low, mid)
        merge_sort(lst, mid + 1, high)
        merge(lst, low, mid, high)

if __name__ == '__main__':
    lst = [1,5,7,2,4,6]

    print(lst)

    merge_sort(lst, 0, 5)

    print(lst)
