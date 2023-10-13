def partition(array: list, low: int, high: int) -> int:
    pivot: int = array[high]
    i: int = low-1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[high] = array[high], array[i]
    return i


def quickSort(array: list, low: int, high: int) -> None:
    if low < high:
        pivotIndex: int = partition(array, low, high)

        quickSort(array, low, pivotIndex-1)
        quickSort(array, pivotIndex+1, high)
