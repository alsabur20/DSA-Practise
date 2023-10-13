def radixSort(arr):
    digits = len(str(max(arr)))
    place = 1
    ans = arr.copy()
    for i in range(digits):
        ans = countSort(ans, place)
        place *= 10
    return ans


def countSort(arr, place):
    n = len(arr)
    maxx = 9
    minn = 0
    rangee = (maxx - minn + 1)
    temp1 = [0] * rangee
    ans = [0] * n
    for num in arr:
        tNum = num // place
        lDigit = tNum % 10
        temp1[lDigit] += 1

    for i in range(1, rangee):
        temp1[i] += temp1[i - 1]

    for num in reversed(arr):
        tNum = num // place
        lDigit = tNum % 10
        temp1[lDigit] -= 1
        ans[temp1[lDigit]] = num
    return ans


if __name__ == "__main__":
    arr = [50, 22, 53, 9, 30]
    print(arr)
    print(radixSort(arr))
    # print(arr)
