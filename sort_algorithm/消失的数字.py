'''
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？

注意：本题相对书上原题稍作改动

示例 1：

输入：[3,0,1]
输出：2
 

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8
'''

'''
    算法思想：用一个长度为n的新数组array[]， 遍历nums数组，把nums[i]放到array[nums[i]]中，遍历结束之后再便利一次array数组；
    没有被赋值的下标就是缺失的数字

'''

class Solution:
    @classmethod
    def missingNumber(self, nums: list[int]) -> int:
        # python记录了列表的长度 o(1)
        length = len(nums)
        tmp = [-1] * (length+1)
        for num in nums:
            tmp[num] = 1
        for index in range(length+1):
            if tmp[index] == -1:
                return index
            
if __name__ == "__main__":
    print(Solution.missingNumber([0,1,2,3,4,6,7]))