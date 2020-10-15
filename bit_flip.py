def flip_bit(bit_array):
    current_length = 0
    previous_length = 0
    max_length = 1
    for i in range(len(bit_array)):
        if bit_array[i] == 1:
            current_length += 1
        if bit_array[i] == 0:
            if i+1 < len(bit_array) and bit_array[i+1] == 0:
                previous_length = 0
            elif i+1 < len(bit_array) and bit_array[i+1] == 1:
                previous_length = current_length
            current_length = 0
    return max(max_length, current_length + previous_length + 1)


array = [1,1,0,1,1,1,0,1,1,1,1]
print(flip_bit(array))

from collections import Counter

