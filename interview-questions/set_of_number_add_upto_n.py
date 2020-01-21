"""
1) Given an Unsorted Array, Find a set of numbers that add up to a certain number.
2) Given an Unsorted Array, Find the count of set of numbers that add up to a certain number.

A set can have any quantity of numbers.
"""

import time


def count_number_of_sets(arr, index, total):
    if total == 0:
        return 1
    elif index > (len(arr) - 1):
        return 0
    elif total < 0:
        return 0
    elif arr[index] > total:
        count = count_number_of_sets(arr, index + 1, total)
    else:
        a = count_number_of_sets(arr, index + 1, (total - arr[index]))
        b = count_number_of_sets(arr, index + 1, total)
        count = a + b

    return count


def count_number_of_sets_memory(arr, index, total, memory):
    key = str(total) + "-" + str(index)
    if key in memory:
        return memory[key]
    elif total == 0:
        return 1
    elif index > (len(arr) - 1):
        return 0
    elif total < 0:
        return 0
    elif arr[index] > total:
        count = count_number_of_sets_memory(arr, index + 1, total, memory)
    else:
        a = count_number_of_sets_memory(arr, index + 1, (total - arr[index]), memory)
        b = count_number_of_sets_memory(arr, index + 1, total, memory)
        count = a + b

    memory[key] = count
    return count


if __name__ == "__main__":
    a = time.time()
    arr = [6, 9, 2, 14, 4, 21, 7, 1, 10, 5, 5]
    m = 14
    print(count_number_of_sets(arr, 0, m))
    b = time.time()
    print("Without Memory: ", b - a)

    a = time.time()
    arr = [6, 9, 2, 14, 4, 21, 7, 1, 10, 5, 5]
    m = 14
    memory = {}
    print(count_number_of_sets_memory(arr, 0, m, memory))
    b = time.time()
    print("With Memory: ", b - a)
    print(memory)
    pass
