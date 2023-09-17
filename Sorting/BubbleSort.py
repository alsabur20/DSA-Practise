#Bubble Sort which sorts the whole array
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

#-------------------------------------------------------------------#
#Bubble Sort which takes in an array and sorts it from start to end                
def BubbleSort(array, start=0, end=None):
    end=len(array)-1 if end==None else end
    for i in range(start, end+1):
        for j in range(start, (start+end)-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                