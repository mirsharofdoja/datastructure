def max_element(arr):
    x=arr[0]
    for i in arr:
        if i>x:
            x=i
    return x
def s_sort(arr):
    new_arr=[]
    while len(arr)!=0:
        new_arr.append(max_element(arr))
        arr.remove(max_element(arr))
    return new_arr
a=[12,56,34,7,33,8,523,5,60]
print(s_sort(a))
