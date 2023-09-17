#Merge Sort that sorts the whole array
def mergeSort(arr):
    n=len(arr)
    if n<=1:
        return arr
    left=mergeSort(arr[0:n/2])
    right=mergeSort(arr[n/2:n])
    return conquer(left,right)
def conquer(left,right):
    merged=[]
    idx1=0
    idx2=0
    while idx1<len(left) and idx2<len(right):
        if left[idx1]<right[idx2]:
            merged.append(left[idx1])
            idx1+=1
        else:
            merged.append(right[idx2])
            idx2+=1
    merged+=left[idx1:]
    merged+=right[idx2:]
    return merged

#-------------------------------------------------------------------#
#Merge Sort which takes in an array and sorts it from start to end
def MergeSort(arr, start=0, end=None):
    end=len(arr)-1 if end==None else end
    if start < end:
        mid = (start + end)//2
        MergeSort(arr, start, mid)
        MergeSort(arr, mid+1, end)
        Merge(arr, start, mid, end)


def Merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]
    i = 0
    j = 0
    k = p
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