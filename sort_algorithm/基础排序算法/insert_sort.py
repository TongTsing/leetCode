from basePackage.base import gen_num_list
from basePackage.base import swapElement


def simpleSort(target:list, length:int)->list:
    # 遍历从第二个元素到最后一个元素
    for i in range(1, length):
        element = target[i]
        j = i - 1
        while j>=0 and element < target[j]:
            target[j+1] = target[j]
            j -= 1
        target[j+1] = element
                
    return target

'''
[64, 103, 35, 7, 101, 3, 1, 2, 2]


'''




if __name__ == '__main__':
    listA = gen_num_list(10)
    simpleSort(listA, length=10)
    print(listA)