def insertion_sort(arr,order = "asc"):
    """This is a Insertion Sort Algorithm which takes Once Element at a Time and 
    Compare with all the previous Elements swap the places until it comes to its 
    rightful place"""
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i] and order == "asc":
            for j in range(i,-1,-1):
                if j-1 >= 0 and arr[j-1] > arr[j]:
                    arr[j-1],arr[j] = arr[j],arr[j-1]
        elif arr[i-1] < arr[i] and order == "desc":
            for j in range(i,-1,-1):
                if j-1 >= 0 and arr[j-1] < arr[j]:
                    arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr

if __name__ == "__main__":
    
    arr = [1,4,6,2,8,3]
    result = insertion_sort(arr,"asc")
    print("--------Test Case: All Positive Elements ")
    print("Ascending:  ",result)
    result = insertion_sort(arr,"desc")
    print("Descending: ",result)

    print("--------Test Case: With Some Negative Elements ")
    arr = [1,4,-6,2,8,3, -9]
    result = insertion_sort(arr,"asc")
    print("Ascending:  ",result)
    result = insertion_sort(arr,"desc")
    print("Descending: ",result)

    print("--------Test Case: Empty Array ")
    arr = []
    result = insertion_sort(arr,"asc")
    print("Ascending:  ",result)
    result = insertion_sort(arr,"desc")
    print("Descending: ",result)

    print("--------Test Case: One Element ")
    arr = [2]
    result = insertion_sort(arr,"asc")
    print("Ascending:  ",result)
    result = insertion_sort(arr,"desc")
    print("Descending: ",result)

    print("--------Test Case: Two Same Elements ")
    arr = [1,4,-6,2,8,3, -6]
    result = insertion_sort(arr,"asc")
    print("Ascending:  ",result)
    result = insertion_sort(arr,"desc")
    print("Descending: ",result)