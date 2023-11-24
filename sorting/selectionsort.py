from typing import List

def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        minindex=i
        for j in range(i,n):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[minindex],arr[i]=arr[i],arr[minindex]
    # print(arr)
    return arr
selectionSort([1,4,3,2])