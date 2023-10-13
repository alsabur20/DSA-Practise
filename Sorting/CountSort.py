def countSort(arr):
    n = len(arr)
    maxx = max(arr)
    minn = min(arr)
    rangee = (maxx - minn + 1)
    temp1 = [0] * rangee
    ans = [0] * n

    for num in arr:
        temp1[num - minn] += 1

    for i in range(1, rangee):
        temp1[i] += temp1[i - 1]

    for num in reversed(arr):
        temp1[num - minn] -= 1
        ans[temp1[num - minn]] = num

    return ans


if __name__ == "__main__":
    arr = [5, 2, 5, 5, -3, 1, 2, 5, 1, 5, 0, 5, 3, -1, 5, 2, 2, 2]
    print(countSort(arr))
