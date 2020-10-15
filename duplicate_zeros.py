def duplicateZeros(arr):
    new_array = []
    length = len(arr)
    for a in arr:
        new_array.append(a)
        if len(new_array) == length:
            break
        if a == 0:
            new_array.append(a)
            if len(new_array) == length:
                break
    arr = new_array
    print(arr)
arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)