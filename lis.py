array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def lis(arr, index, prev):
    if index >= len(arr):
        return 0
    
    # compare including the current one and excluding the current one
    incl = 0 
    if arr[index] > prev:
        prev = arr[index]
        incl = 1 + lis(arr, index + 1, prev)
    excl =lis(arr, index + 1, prev)
    return max(incl, excl)

print(lis(array, 0, -999999))

solution = [None for x in range(len(array))]
print(solution)
solution[0] = 1
# wrong write again
for i in range(1, len(array)):
    if array[i] > array[i-1]:
        solution[i] = solution[i-1] + 1
    else:
        solution[i] = solution[i-1]
print(solution)
