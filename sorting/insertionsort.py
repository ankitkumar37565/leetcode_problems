def insertionSort(arr,n):
    # print(arr)
    for i in range(1,n):
        selected=i
        while (selected>0 and arr[selected-1]>arr[selected]):
            arr[selected],arr[selected-1]=arr[selected-1],arr[selected]
    # print(arr)
    return arr
insertionSort([2, 13, 4, 1, 3, 6, 28],5)
            