def selection_sort(arr,order = "asc"):
    """
    Selection Sort is a O(n**2) sorting algorithm which loops through the list to find shortest  
    and replaces it with the front of the list and iterates a step to find the next minimum in 
    the remainder of the list until the list and so on..

    Mistake in the Inner Loop : Used Enumerate without the start parameter. Enumerate will always start the loop with 0.
    """
    for itr in range(len(arr)):
        if len(arr) < 2:
            return arr
        # Min for ASC and Max for DESC
        index = itr
        for idx,number in enumerate(arr[itr:], start = itr):
            if order == "asc" and number < arr[index]:
                index = idx
            elif order == "desc" and number > arr[index]:
                index = idx
        arr[itr], arr[index] = arr[index], arr[itr]
    return arr

if __name__ == "__main__":
    print("Ascending Order : ",selection_sort([3,7,2,9,4,7,10.5],"asc"))
    print("Descending Order: ",selection_sort([3,7,2,9,4,7,10.5],"desc"))
    
