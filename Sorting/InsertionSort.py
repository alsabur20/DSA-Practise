# Insertion Sort Algorithm

arr = [7, 8, 3, 1, 2]

def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr


print(insertionSort(arr))
