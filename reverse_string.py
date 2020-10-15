def reverse_string(arr):
    if len(arr) == 0:
        return
    s = arr.pop(0)
    reverse_string(arr)
    arr.append(s)
    return arr

print(reverse_string(['1', '2', '3', '4']))