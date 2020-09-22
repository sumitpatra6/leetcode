def find_sum(array, start_x, start_y, end_x, end_y):
    print(start_x, start_y, end_x, end_y)
    sum = 0
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            sum += array[i][j]
    print(sum)
    return sum

def find_subset(array, start_x, start_y, end_x, end_y, row, column):
    if find_sum(array, start_x, start_y, end_x, end_y) == 0:
        return 1
    if start_x >= row or start_y >= column or end_x >= row or end_y >= column:
        return 0
    for i in range(start_x, end_x +1):
        for j in range(start_y, end_y + 1):
            # find recursively for each subset 
            return find_subset(array, start_x, start_y, end_x, end_y, row, column) + \
                    find_subset(array, start_x, start_y, end_x+1, end_y, row, column) + \
                        find_subset(array, start_x, start_y, end_x, end_y+1, row, column) + \
                            find_subset(array, start_x, start_y, end_x +1, end_y +1, row, column)



array = [[0,1,0],[1,1,1],[0,1,0]]
print(find_subset(array, 0,0,0,0, len(array), len(array[0])))
