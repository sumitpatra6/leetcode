def pattern_match(string, pattern):
    n = len(string)
    m = len(pattern)
    solution = [[False for _ in range(m+1)] for _ in range(n+1)]
    print(solution)
    # initialize the solution
    solution[0][0] = True
    for j in range(1, m+1):
        if pattern[j-1] == "*":
            solution[0][j] = solution[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[j-1] == '*':
                solution[i][j] = solution[i-1][j] or solution[i][j-1]
            elif pattern[j-1] == '?' or pattern[j-1] == string[i-1]:
                solution[i][j] = solution[i-1][j-1]
            else:
                solution[i][j] = False
    print(solution)
    print(solution[n][m])


string = 'baabab'
pattern = "ba*a?"
pattern_match(string, pattern)