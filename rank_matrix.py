input_matrix = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k = 3
original_array = [i for i in range(len(input_matrix))]
print(type(original_array))
def sort_array(input_matrix, original_array):
    print("Sortng arrray")
    original_array.sort(key=lambda x: sum(input_matrix[x]))
    return original_array

sorted_original_array = sort_array(input_matrix, original_array)
print(sorted_original_array[:k])