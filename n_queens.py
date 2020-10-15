array = []
count = 0
n = 4

def is_safe(row, col):
    # first check if there is a queen in the same row or column
    for i in range(n):
        if array[row][i] == 1 or array[i][col] == 1:
            return False
    i = 0
    for i in range(n):
        for j in range(n):
            if i+j == row+col or i -j == row - col:
                if array[i][j] == 1:
                    return False
    return True

def solve_n_queens(row=0, count=0):
    for col in range(n):
        # check if the cell if safe
        if is_safe(row, col):
            # place the queen here
            array[row][col] = 1
            if row + 1 == n:
                # reached the last row, combination found
                print(array)
                count += 1
                print(count)
            else:
                count = solve_n_queens(row+1, count)
            array[row][col] = 0
    return count


def n_queens(n):
    global array
    array = [[0 for _ in range(n)] for _ in range(n)]
    print(solve_n_queens())

n_queens(n)