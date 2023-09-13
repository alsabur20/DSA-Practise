#Merge Sort Algorithm

#Code for mergesort algorithm
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