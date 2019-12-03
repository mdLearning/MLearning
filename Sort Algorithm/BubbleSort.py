def Bubble_Sort(arr):
    n = len(arr)
    if n<=1:
        return arr
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__=='__main__':
    x=input('input list:\n')
    y = x.split()
    arr = []
    for i in y:
        arr.append(int(i))
    arr = Bubble_Sort(arr)
    print('after bubble sort:\n')
    for j in arr:
        print(j,end=' ')
