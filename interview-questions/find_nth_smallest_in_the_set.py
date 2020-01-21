"""
Find the Nth Order Statistic for a given array of numbers
Steps : 
Find the Smallest Number - 
    this is straightforward O(n), 
Find 2nd Smallest Number - 
    Brute Force - Find Minimum - swap with 1st element - then again loop the remainder to find 2nd shortest - O(n**2)
    Best Possible - Have two index - 1st will store the minimum, 2nd will store the 2nd min and them comparing them with rest of the list and comparing with each other. O(n)

Find Nth Smallest - 
    Take any element and place it in its correct position.
    Comapare this position with N if N is smaller recurse 1st half else 2nd half.

    Time Complexity : O(n)
    Time Analysis:
        This uses partition logic of quicksort algorithm.. which is done in O(n) time. In our case everytime the lookup for array becomes half the previous size considering Average Case.
        Hence, the series of going through the array is like n + n/2 + n/4 + n/8 + n/16 .... which become (n).
    Space Complexity: O(1)
"""


def findShortestInList(arr):
    min = arr[0]
    for num in arr[1:]:
        if num < min:
            num, min = min, num
    return min


def findSecondShortestInList(arr):
    min1 = arr[0]
    min2 = arr[1]
    for index in enumerate(arr[2:], start=2):
        if arr[index] < min2:
            arr[index], min2 = min2, arr[index]
        elif arr[index] < min1:
            arr[index], min1 = min1, arr[index]
        if min2 < min1:
            min1, min2 = min2, min1
    return min2


def findNthShortestInList(arr, n):
    position = partition(arr)
    if n < position:
        return findNthShortestInList(arr[:position], n)
    elif n > position:
        return findNthShortestInList(arr[position:], (n - position))
    else:
        return arr[position]


def partition(arr):
    l = len(arr)
    if l > 1:
        pivot = arr[l - 1]
        position = 0
        for number in range(0, l - 1):
            if arr[number] <= pivot:
                arr[position], arr[number] = arr[number], arr[position]
                position += 1
        arr[position], arr[l - 1] = arr[l - 1], arr[position]
        return position


if __name__ == "__main__":
    arr = [4, 7, 2, 9, 1, 10, 45, 21, 15, 31, 13, 41, 14, 68, 18]
    print(arr)
    min = findShortestInList(arr)  # O(n)
    print(min)

    arr = [4, 7, 2, 9, 1, 10, 45, 21, 15, 31, 13, 41, 14, 68, 18]
    min = findSecondShortestInList(arr)  # O(n)
    print(min)

    arr = [4, 7, 2, 9, 1, 10, 45, 21, 15, 31, 13, 41, 14, 68, 18]
    n = 10
    min = findNthShortestInList(arr, n - 1)  # O(n)
    print(min)
