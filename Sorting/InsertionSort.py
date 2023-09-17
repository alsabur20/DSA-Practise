# Insertion Sort which sorts the whole array
def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

#-------------------------------------------------------------------#
#Insertion Sort which takes in an array and sorts it from start to end
def InsertionSort(arr, start=0, end=None):
    end=len(arr)-1 if end==None else end
    for i in range(start + 1, end+1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
