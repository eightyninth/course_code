# For O(log n)
import time
import numpy as np

def binary_search(arr, tar):
    exec_num = 0
    res = -1
    arr_len = len(arr)
    left, right, mid = 0, arr_len - 1, arr_len // 2

    start_time = time.time()
    while left <= right:
        if arr[mid] > tar:
            right = mid - 1
        elif arr[mid] < tar:
            left = mid + 1
        else:
            res = mid
            break
        exec_num += 1
        mid = (left + right) // 2
    end_time = time.time()

    print("Binary Search Execution time: ", (end_time - start_time) * 1000)
    print("Binary Search Execution nume: ", exec_num)

    return res


if __name__ == '__main__':
    arr20000 = np.sort(np.random.randint(0, 10000, 20000))
    arr100000 = np.sort(np.random.randint(0, 10000, 100000))

    x = np.random.randint(0, 100)

    binary_search(arr20000, x)
    binary_search(arr100000, x)
