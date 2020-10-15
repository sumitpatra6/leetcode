N = 4
board = []
for i in range(N):
    board.append([0]*N)

results = []
def is_under_attack(i, j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return False
    for k in range(N):
        for l in range(N):
            if k+l == i+j or k -l == i - j:
                if board[k][l] == 1:
                    return False
        
    return False

def back_track_nqueen(row=0, count=0):
    for col in range(N):
        if not is_under_attack(row, col):
            board[row][col] = 1
            if row + 1 == N:
                count += 1
                results.append(board)
            else:
                count = back_track_nqueen(row + 1, count)
            board[row][col] = 0
    return count

print(back_track_nqueen())
print(results)