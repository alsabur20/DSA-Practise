#Selection Sort which sorts the whole array
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

#-------------------------------------------------------------------#
#Selection Sort which takes in an array and sorts it from start to end
def SelectionSort(arr, start=0, end=None):
    end=len(arr)-1 if end==None else end
    for i in range(start, end+1):
        smallest = i
        for j in range(i+1, end+1):
            if arr[j] < arr[smallest]:
                smallest = j
        temp = arr[smallest]
        arr[smallest] = arr[i]
        arr[i] = temp