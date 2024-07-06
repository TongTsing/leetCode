import time
from basePackage.base import *

'''
1 3 7 9
2 4 6 8
'''

def merge(target1: list, target2: list, length1: int, length2: int) -> list:
    tmpList = []
    index1 = 0
    index2 = 0
    while index1 < length1 and index2 < length2:
        if target1[index1] < target2[index2]:
            tmpList.append(target1[index1])
            index1 += 1
        else:
            tmpList.append(target2[index2])
            index2 += 1
    if index1 != length1:
        tmpList.extend(target1[index1: length1])
    if index2 != length2:
        tmpList.extend(target2[index2: length2])
    return tmpList


def merge_sort_recursion(target: list, left: int, right: int) -> list:
    if left < right:
        mid = (left + right) // 2  # 使用整数除法
        merge_sort_recursion(target, left, mid)
        merge_sort_recursion(target, mid + 1, right)
        # 合并两个已排序的子数组
        merged = merge(target1=target[left:mid+1], target2=target[mid+1:right+1], length1=mid-left+1, length2=right-mid)
        target[left:right+1] = merged  # 将合并后的结果复制回原数组
    return target


'''
    非递归算法
'''

def merge_sort(target: list, left:int, right: int)->list:
    # 非递归算法思想： n个元素可以看作n个一排序长度为1的子序列，
    # 然后把相邻的两个元素做一次归并，这样就得到了长度为2的n/2个有序子列，同理再进行归并
    # 2 7 0 9 3 8  7 5 2 4 
    step = 1
    n = right - left + 1
    while step < n:
        for i in range(0, n, 2 * step):
            mid = min(left + i + step - 1, right)
            end = min(left + i + 2 * step - 1, right)
            if mid < end:
                merged = merge(target[left + i:mid + 1], target[mid + 1:end + 1], mid - (left + i) + 1, end - mid)
                target[left + i:end + 1] = merged
        step *= 2
    return target

if __name__ == '__main__':
    length1 = 10000000
    length2 = 5
    list1 = gen_num_list(length1)
    list2 = gen_num_list(length2)
    start_time = time.time()
    res = merge_sort(list1, 0, length1-1)
    print(list1)
    print(res[-100:])

    print(f"耗时： {time.time()-start_time}")