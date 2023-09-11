# print string reversed
def reverseString(string, idx):
    if idx == 0:
        return string[idx]
    return string[idx] + reverseString(string, idx-1)


s = 'abcd'
# print(reverseString(s,len(s)-1))

# Find the 1st and last occurence of an element in string

first = -1
last = -1


def findOccurance(str, idx, element):
    global first, last
    if idx == len(str):
        print(first, last)
        return
    currentChar = str[idx]
    if currentChar == element:
        if first == -1:
            first = idx
        else:
            last = idx
    findOccurance(str, idx+1, element)

# findOccurance("abaacdaefaah",0,'a')

# Check if an array is sorted (Strictly increasing)


def isSorted(arr, idx):
    if idx == len(arr)-1:
        return True
    if arr[idx] >= arr[idx+1]:
        return False
    return isSorted(arr, idx+1)

# print(isSorted([1,2,3,4],0))