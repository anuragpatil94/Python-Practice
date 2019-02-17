def quick_sort(arr,low,high):
    if(low < high):
        pivotPosition = partition(arr,low,high)
        quick_sort(arr,low,pivotPosition - 1)        
        quick_sort(arr,pivotPosition + 1, high)        

def partition(arr, low, high):
    pivot = arr[high]
    minIndex = low
    for index in range(low,high):
        if arr[index] <= pivot:
            arr[minIndex],arr[index] = arr[index],arr[minIndex]
            minIndex = minIndex + 1
    arr[minIndex],arr[high] = arr[high],arr[minIndex]
    return minIndex
            

if __name__ == "__main__":
    arr = [13,11,5,12,3,9,16,10]
    quick_sort(arr,0,len(arr)-1)
    print(arr)