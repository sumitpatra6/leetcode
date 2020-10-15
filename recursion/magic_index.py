array = [-10, -5, 2,2,2,3,4,7,9,12,13]

def find_magic_index(array):
    start = 0
    end = len(array) - 1
    return find(array, start, end)

def find(array, start, end):
    if end < start:
        return -1
    middle = int((start  + end) / 2)
    mid_val = array[middle]
    if middle == mid_val:
        return middle
    left_index = min(mid_val, middle - 1)
    left = find(array, start, left_index)
    if left >= 0:
        return left
    right_index = max(middle +1, mid_val)
    right = find(array, right_index,end)
    return right

print(find_magic_index(array))