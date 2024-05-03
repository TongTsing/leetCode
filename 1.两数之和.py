import copy
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。

# 示例 1：
#
# 输入：nums = [2,4,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 要求：时间复杂度小于O(n^2)
# 算法思想：做一次快速排序，nlogn， 一次二分查找的时间复杂度为logn,n次为nlogn; 排序后就是在找target - sums[index]是否存在于数组中；
# 然后再根据元素找到原始位置空间复杂度n, 时间复杂度n
# n + 2nlogn << n^2


#[2, 4, 7, 11, 15]
#[2, 4, 7, 11, 15]
#[15, 11, 7, 4, 2]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None  # 如果目标不在数组中
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tmpNums = copy.copy(nums)
        tmpNums.sort()
        # print(tmpNums)
        for i in tmpNums:
            tmpTarget = target - i
            search_result = binary_search(tmpNums, tmpTarget)
            # print(i, search_result)
            if search_result == None:
                continue
            else:
                result = []
                for j in range(len(nums)):
                    if nums[j] == i or nums[j] == search_result:
                        result.append(j)
                        print(j,nums[j], i, search_result)
                return result
    # 示例
if __name__ == '__main__':
    arr = [2,7,11,15]
    target = 9
    ins = Solution()
    print(ins.twoSum(arr,target))


