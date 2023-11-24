def bubbleSort(arr,n):
    # n=len(arr)
    for i in range(n-1,0,-1):    
        max=0
        for j in range(1,i+1):
            if arr[j]>arr[max]:
                max=j
        arr[i],arr[max]=arr[max],arr[i]
    return arr
# bubbleSort([2,3,4,45,12,10])