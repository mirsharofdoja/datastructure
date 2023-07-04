def b_search(arr,x):
    l=0
    h=len(arr)-1
    while h>=l:
        m=(l+h)//2
        if arr[m]==x:
            return m
        elif a[m]<x:
            l=m+1
        else:
            h=m-1
    return None
a=[1,3,4,6,7,8,10,12,23,45,56,78,99,100]
print(b_search(a,5))