import BubbleSort
import SelectSort
import InsertSort
import MergeSort

if __name__=='__main__':
    x=input('input list:\n')
    y = x.split()
    arr = []
    for i in y:
        arr.append(int(i))
    arr = MergeSort.MergeSort(arr)
    print('after bubble sort:\n')
    for j in arr:
        print(j,end=' ')