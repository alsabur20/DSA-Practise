#Hybrid Merge Sort using Insertion Sort
def InsertionSort(arr, start=0, end=None):
    end=len(arr)-1 if end==None else end
    for i in range(start+1, end+1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def HybridMergeSort(arr, start=0, end=None, threshold=None):
    end=len(arr)-1 if end==None else end
    threshold=10 if threshold==None else threshold
    if (end - start + 1) <= threshold:
        InsertionSort(arr, start, end)
    else:
        mid = (start+end)//2
        HybridMergeSort(arr, start, mid, threshold)
        HybridMergeSort(arr, mid+1, end, threshold)
        Merge(arr, start, mid, end)

def Merge(arr, start, mid, end):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1