import numpy as np
import random

def split(array):
    border = int(len(array) / 2)
    part_1 = array[0:border]
    part_2 = array[border:]

    return part_1, part_2

def merge(part_1, part_2):
    i, j, k = 0, 0, 0
    len_1 = len(part_1)
    len_2 = len(part_2)
    res_len = len_1 + len_2
    result = np.zeros((res_len))

    while (i < len_1) & (j < len_2):
        if (part_1[i] < part_2[j]):
            result[k] = part_1[i]
            k = k + 1
            i = i + 1
        else:
            result[k] = part_2[j]
            k = k + 1
            j = j + 1

    return result


def merge_sort(array):
    if (len(array) == 1):
        return array
    else:
        part_1, part_2 = split(array)

    return merge(merge_sort(part_1), merge_sort(part_2))

if __name__ == "__main__":
    print('investigating merge sort')

    unsorted_arr = random.sample(range(1000), k = 50)
    print('\nunsorted_arr = ', unsorted_arr)
    sorted_arr = merge_sort(unsorted_arr)
    print('\nsorted_arr = ', sorted_arr)
