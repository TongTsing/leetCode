import random

def gen_num_list(length)->list:
    result = []
    for i in range(length):
        result.append(random.randint(1, length*100))
    return result