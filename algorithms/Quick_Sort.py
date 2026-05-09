# For O(n log n)
import time
import numpy as np

def partition(arr, low, high, ascending, exec_num):
    """
    快速排序的分治算法
    :param arr: 待排序数组
    :param low: 数组起始位置
    :param high: 数组结束位置
    :param ascending: True 为小到大, False 为大到小
    :param exe_num: 操作次数
    :return: 分割点, 操作次数
    """
    pivot = arr[high]
    i, j = low, high
    while i < j:
        if ascending:
            while i < j and arr[i] <= pivot:
                i += 1
                exec_num += 1
            while i < j and arr[j] >= pivot:
                j -= 1
                exec_num += 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            while i < j and arr[i] >= pivot:
                i += 1
                exec_num += 1
            while i < j and arr[j] <= pivot:
                j -= 1
                exec_num += 1
            arr[i], arr[j] = arr[j], arr[i]
        exec_num += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i, exec_num

def quick_sort(arr, low, high, ascending, exec_num):
    """
    快速排序
    :param arr: 待排序数组
    :param low: 数组起始位置
    :param high: 数组结束位置
    :param ascending:  True 为小到大, False 为大到小
    :param exe_num: 操作次数
    """
    if high - low < 1: return exec_num
    mid_idx, exec_num = partition(arr, low, high, ascending, exec_num)
    exec_num = quick_sort(arr, low, mid_idx - 1, ascending, exec_num)
    exec_num = quick_sort(arr, mid_idx, high, ascending, exec_num)

    return exec_num

if __name__ == '__main__':
    arr2000 = np.random.randint(0, 10000, 2000)
    arr5000 = np.random.randint(0, 10000, 5000)

    tmp = [5,5,3,67,8,0,9,2,1,4,6,7]
    res = quick_sort(tmp, 0, 11, True,0)

    start_time = time.time()
    exec_num = quick_sort(arr2000, 0, len(arr2000) - 1,True,0)
    end_time = time.time()
    print("Quick Sort Execution time: ", (end_time - start_time) * 1000)
    print("Quick Sort Execution nume: ", exec_num)

    start_time = time.time()
    exec_num = quick_sort(arr5000,  0, len(arr5000) - 1,True,0)
    end_time = time.time()
    print("Quick Sort Execution time: ", (end_time - start_time) * 1000)
    print("Quick Sort Execution nume: ", exec_num)
