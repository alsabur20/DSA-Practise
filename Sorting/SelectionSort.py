#Selection Sort Algorithm

def selectionSort(arr):
    for i in range(len(arr)-1):
        smallentIndex=i
        for j in range(i+1,len(arr)):
            if arr[smallentIndex]>arr[j]:
                smallentIndex=j
        temp=arr[smallentIndex]
        arr[smallentIndex]=arr[i]
        arr[i]=temp
    return arr

arr=[7,8,3,1,2]
print(selectionSort(arr))