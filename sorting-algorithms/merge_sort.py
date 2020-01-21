import math

"""This is one the most commonly used Sorting Algorithm which has the Time Complexity of O(n log n)"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = math.ceil(len(arr) / 2)
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Sort only for those elements for least length
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy rest of the elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [13, 11, 5, 12, 3, 9, 16]
    merge_sort(arr)
    print(arr)
