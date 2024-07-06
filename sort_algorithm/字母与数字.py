'''
面试题 17.05. 字母与数字
中等

相关标签
相关企业

提示
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

示例 1:

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
示例 2:

输入: ["A","A"]

输出: []

'''


# 要找到一个包含相同数量的字母和数字的最长子数组，可以使用哈希表来记录每个前缀和的首次出现位置，从而在一次遍历中实现解决问题的目标。具体思路如下：

# 1. 使用一个哈希表记录每个前缀和首次出现的位置。
# 2. 定义一个变量 `balance`，用于表示当前前缀和。遍历数组时，如果遇到字母就加1，遇到数字就减1。
# 3. 遍历数组时，更新 `balance`，并在哈希表中查找该 `balance` 是否已经出现过。如果出现过，计算当前子数组的长度并更新最长子数组的起止位置。
# 4. 如果 `balance` 首次出现，则将其记录在哈希表中。

# 这样可以在一次遍历中找到最长的符合条件的子数组。

# 以下是Python实现代码：

def findLongestSubarray(array):
    balance_map = {0: -1}  # 初始化哈希表，记录前缀和为0的位置为-1
    balance = 0
    max_length = 0
    start_index = 0
    
    for i, char in enumerate(array):
        if char.isdigit():
            balance -= 1
        else:
            balance += 1
        
        if balance in balance_map:
            length = i - balance_map[balance]
            if length > max_length:
                max_length = length
                start_index = balance_map[balance] + 1
        else:
            balance_map[balance] = i
    
    return array[start_index:start_index + max_length]

# 示例测试
array1 = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
print(findLongestSubarray(array1))  # 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]

array2 = ["A","A"]
print(findLongestSubarray(array2))  # 输出: []

### 代码说明：
# 1. `balance_map` 记录每个前缀和首次出现的位置。初始值 `{0: -1}` 表示在遍历开始前，前缀和为0的位置是-1。
# 2. 遍历数组，根据字符类型更新 `balance`。遇到字母加1，遇到数字减1。
# 3. 如果 `balance` 已经在 `balance_map` 中出现过，计算当前子数组的长度。如果比记录的最大长度大，则更新最大长度和起始位置。
# 4. 如果 `balance` 尚未出现，将其添加到 `balance_map` 中。
# 5. 最后，根据记录的起始位置和最大长度返回最长子数组。

# 这个方法的时间复杂度为O(n)，空间复杂度为O(n)，能够高效地找到符合条件的最长子数组。
# ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
#
