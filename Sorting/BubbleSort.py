#Bubble Sort Algorithm

arr=[7,8,3,1,2]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                
    return arr

print(bubbleSort(arr))