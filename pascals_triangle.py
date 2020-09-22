def get_pascal_row(i, j):
    if j == i or j == 1:
        return 1
    else:
        return get_pascal_row(i-1, j-1) + get_pascal_row(i-1, j)


row_index = 3
no_of_column = row_index + 1
ret_value = []
for i in range(1, no_of_column+1):
    ret_value.append(get_pascal_row(3, i))

print(ret_value)