from basePackage.base import *


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    arrayA = gen_num_list(10000000)
    arrayA_sorted = quicksort(arrayA)
    print(arrayA_sorted[-10:])