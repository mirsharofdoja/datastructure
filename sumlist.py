def sum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr.pop()+sum(arr)
