X = 'ABCBDAB'
Y = 'BDCABA'

#recursive

def lcs_recursive(X, Y, m, n):
    # base condition
    if m ==0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m -1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m -1, n), lcs_recursive(X, Y, m, n - 1))

print(lcs_recursive(X, Y, len(X), len(Y)))

#write code nonrecursive

solution = [[0 for x in range(len(X) + 1)] for y in range(len(Y) + 1)]
for i in range(1, len(Y) + 1):
    for j in range(1, len(X) + 1):
        if Y[i-1] == X[j-1]:
            solution[i][j] = 1 + solution[i -1][j-1]
        else:
            solution[i][j] = max(solution[i -1][j], solution[i][j-1])

for x in solution:
    print(x)
