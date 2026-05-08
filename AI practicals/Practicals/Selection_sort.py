def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

arr=[60,11,13,20,32,8]
print(f'\nArray before sorting: {arr}')
selection_sort(arr)
print(f'\nArray after sorting: {arr}')
