X = 'kitten'
Y = 'siting'

def minimum_distance(X, Y, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if X[m -1] == Y[n -1]:
        cost = 0
    else: 
        cost = 1
    return min(minimum_distance(X, Y, m-1, n) + 1, \
            minimum_distance(X, Y, m, n-1) + 1, \
            minimum_distance(X, Y, m -1, n -1) + cost)

print(minimum_distance(X, Y, len(X), len(Y)))
