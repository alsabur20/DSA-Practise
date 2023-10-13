import math
from countSort import countSort


def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def bucketSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        bucketNumber = math.floor(num * n)
        bucket = buckets[bucketNumber]
        bucket.append(num)
    for bucket in buckets:
        insertionSort(bucket)
    ans = [row[j] for row in buckets for j in range(len(row))]
    return ans


if __name__ == '__main__':
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(arr)
    print(bucketSort(arr))
