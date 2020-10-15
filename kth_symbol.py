"""Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Recurrent relation:-
f(i,j) = if j % 2 == 0 then f[i-i, j/2] else !f[i-1, j/2]
base condition
if i == 0 and j == 0 return 0
"""

def kthGrammar(N, K):
    if N == 1:
        return 0
    prev_index = K/2
    digit = kthGrammar(N-1, prev_index)
    if digit == 0:
        return 0 if K %2 ==0 else 1
    else:
        return 1 if K %2 == 1 else 0
print(kthGrammar(1, 1))
print(kthGrammar(2, 1))
print(kthGrammar(2, 2))
print(kthGrammar(4, 5))