def l_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return None

a=[1,3,4,6,7,8,10,12,23,45,56,78,99]
print(l_search(a,99))