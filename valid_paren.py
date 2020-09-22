class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        str = list(S)
        container = []
        while len(str) > 0:
            if len(str) == 1:
                if len(container) > 0 and container[-1] == '(' and str[0] == ')':
                    container.pop()
            last = str.pop()
            curr = str[-1]
            if last == ')' and curr == '(':
                str.pop()
            elif last == ')' and len(container) > 0 and container[-1] == '(':
                
            curr = str.pop()
            last = s
                
sol = Solution()
 
inp = "())"
print(1)
print(sol.minAddToMakeValid(inp))
inp = "((("
print(3)
print(sol.minAddToMakeValid(inp)) 
inp = "()"
print(0)
print(sol.minAddToMakeValid(inp))
inp = "()))(("
print(4)
print(sol.minAddToMakeValid(inp))
inp = "((())"
print(1)
print(sol.minAddToMakeValid(inp))
inp = ")()(())))("
print(4)
print(sol.minAddToMakeValid(inp))