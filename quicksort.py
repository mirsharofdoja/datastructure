from random import randrange
def q_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr.pop(randrange(len(arr)))
        kichik=[i for i in arr if i<pivot]
        katta=[i for i in arr if i>pivot]
        return q_sort(kichik)+[pivot]+q_sort(katta)
print(q_sort([4,854,52,566,7,1,669,51,2,0,71]))