def b_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(b_sort([64, 34, 25, 12, 22, 11, 90]))