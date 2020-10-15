def trap_water(array):
    length = len(array)
    left = [0]*length
    right = [0] * length
    left[0] = array[0]
    for i in range(1, length):
        left[i] = max(left[i-1], array[i])
    right[length-1] = array[length-1]
    for i in range(length-2, -1, -1):
        right[i] = max(right[i+1], array[i])
    print(array)
    print(left)
    print(right)
    # calculate the trapped water
    total = 0
    for i in range(length):
        total += min(left[i], right[i]) - array[i]
    print(total)


array = [0,1,0,2,1,0,1,3,2,1,2,1]
trap_water(array)