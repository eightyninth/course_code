# For O(n ^ 2)
import time
import numpy as np

def bubble_sort(arr, sorted):
    """
    冒泡排序
    :param arr: 待排序数组
    :param sorted: True 为小到大, False 为大到小
    """
    exec_num = 0
    arr_len = len(arr)

    start_time = time.time()
    for i in range(arr_len - 1):
        for j in range(arr_len - i - 1):
            if sorted:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            exec_num += 1
    end_time = time.time()

    print("Bubble Sort Execution time: ", (end_time - start_time) * 1000)
    print("Bubble Sort Execution nume: ", exec_num)

if __name__ == '__main__':
    arr2000 = np.random.randint(0, 10000, 2000)
    arr5000 = np.random.randint(0, 10000, 5000)

    bubble_sort(arr2000, True)
    bubble_sort(arr5000, True)
