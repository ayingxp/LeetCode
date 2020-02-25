import os



# quick sort

def partition(data, left, right):
    """
    做一次完整的分割，即把left到right部分中小于data[0](pivot)的数据排在左边，
    :把大于pivot的部分放在右边
    """
    tmp = data[left]

    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]

        while left < right and data[left] <= tmp:
            left += 1

        data[right] = data[left]

    data[left] = tmp
    
    return left




def quick_sort(data, left, right):
    if left < right:  # at least two elements in data
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)



if __name__ == '__main__':
    data = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    print(data)
    quick_sort(data, 0, len(data) -1)
    print(data)

