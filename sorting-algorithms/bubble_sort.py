def bubble_sort(arr, order="asc"):
    """A Non-Recursive Approach for Bubble Sort Algorithm. It can be considered as a brute-force approach to sort"""
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i] and order == "asc":
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[j] > arr[i] and order == "desc":
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


if __name__ == "__main__":
    bubble_sort([1, 4, 2, 7, 5], "desc")
