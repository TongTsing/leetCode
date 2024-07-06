import random

def gen_num_list(length)->list:
    result = []
    for i in range(length):
        result.append(random.randint(1, length*2))
    return result


def swapElement(tmpList: list, index1: int, index2: int):
    tmpList[index1], tmpList[index2] = tmpList[index2], tmpList[index1]