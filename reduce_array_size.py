input_array = [3,3,3,3,5,5,5,2,2,7]


def get_min_count(array, index, visited, minimum):
    if index >= len(array):
        return minimum
    count_current_numbers = 0
    
    for i in range(index, range(array)):
        if array[i] not in visited:
            count_current_numbers += 1
    if count_current_numbers < minimum:
        minimum = count_current_numbers
    for i in range(index, len(array)):
        return min(minimum, get_min_count(array, i, visited, minimum))

print(get_min_count(input_array, 0, [], len(input_array)))