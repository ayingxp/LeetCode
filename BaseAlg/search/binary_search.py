import time



def binary_search(lst, target):
    if not lst:
        print('lst is empty!')
        return None

    if target < lst[0] or target > lst[-1]:
        print('target is not in range!')
        return None

    left = 0
    right = len(lst) - 1
    mid = (left + right) // 2

    while True:
        if left > right:
            return None
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid
            mid = (left + right) // 2
        elif lst[mid] < target:
            left = mid
            mid = (left + right) // 2


    


if __name__ == '__main__':
   lst = list(range(10000)) 
   
   
   target = 8888
   s = time.time()
   ind = binary_search(lst, target)
   e = time.time()

   print(ind)
   print(e-s)
   print(lst[ind])
