def InsertSort(arr):
    n = len(arr)
    if n <= 1 :
        return arr
    for i in range(1, n):
        j = i
        target = arr[i]
        while j>0 and target < arr[j-1]:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = target
    return arr