'''
希尔排序（Shell Sort）是插入排序的一种更高效的改进版本，也被称为递减增量排序算法。
它通过比较一定间隔的元素来进行排序，随着算法的进行，这个间隔逐渐减小，最终使整个数组有序。
希尔排序的效率在很大程度上取决于所使用的增量序列。

算法实现：只需要在insert_sort的基础上外部加一个循环变量增量（step）列表，然后把insert_sort中索引计算中的1改成step就可以了


'''


from basePackage.base import gen_num_list
from basePackage.base import swapElement
import time

def simpleSort(target:list, length:int, step:int)->list:
    # 遍历从第二个元素到最后一个元素
    for i in range(1, length):
        element = target[i]
        j = i - step
        while j>=0 and element < target[j]:
            target[j+step] = target[j]
            j -= step
        target[j+step] = element
    return target

# 定义Hibbard增量序列的迭代器
def hibbard_sequence(n):
    """Generate Hibbard increment sequence for a given n."""
    k = 1
    while (2 ** k - 1) < n:
        yield 2 ** k - 1
        k += 1

def shell_sort(target: list, length: int)->list:
    for i in hibbard_sequence(length):
        simpleSort(target=target, length=length, step=i)
    return target

'''
 0    1    2    3    4    5     6    8    8]
[64, 103, 35,   7,  101,  3,    1,   2,   2]
step=2
a     b    a    b    a    b     a    b    a


'''




if __name__ == '__main__':
    length = 30000
    listA = gen_num_list(length=length)
    startTime = time.time()
    shell_sort(listA, length=length)
    print(listA[-20:-1])
    print(f'耗时: {time.time()-startTime}')