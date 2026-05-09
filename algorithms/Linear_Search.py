# For O(n)
import time
import numpy as np

def linear_search(arr, tar):
    exec_num = 0
    res = -1

    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == tar:
            res = i
            break
        exec_num += 1

    end_time = time.time()

    print("Linear Search Execution time: ", (end_time - start_time) * 1000)
    print("Linear Search Execution nume: ", exec_num)
    return res

if __name__ == '__main__':
    arr20000 = np.random.randint(0, 10000, 20000)
    arr100000 = np.random.randint(0, 10000, 100000)

    x = np.random.randint(0, 100)

    result20000 = linear_search(arr20000, x)
    result100000 = linear_search(arr100000, x)
