def power_set(array, subset, index):
    print(*subset)
    for i in range(index, len(array)):
        subset.append(array[i])
        power_set(array, subset, i+1)
        subset.pop(-1)
    return


array = [1,2,3]
power_set(array, [], 0)