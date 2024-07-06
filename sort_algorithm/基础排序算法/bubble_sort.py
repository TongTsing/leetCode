import random
import time


def gen_num_list(length)->list:
    result = []
    for i in range(length):
        result.append(random.randint(1, length*100))
    return result

def swapElement(tmpList: list, index1: int, index2: int):
    tmpList[index1], tmpList[index2] = tmpList[index2], tmpList[index1]

def bubble_sort(target: list, length: int) -> list:
    for out_index in range(length):
        flag = 0
        for inner_index in range(length-out_index-1):
            if target[inner_index] > target[inner_index+1]:
                swapElement(target, index1=inner_index, index2=inner_index+1)
                flag = 1
        if flag == 0:
            return target
    return target
    
            


if __name__ == "__main__":
    length = 30000
    lista = gen_num_list(length)
    startTime = time.time()
    bubble_sort(lista, length)
    print("used time: ", time.time() - startTime)