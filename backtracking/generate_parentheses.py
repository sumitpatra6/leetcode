count = 0
def generate_parentheses(n):
    string = ""
    for i in range(n):
        string += "()"
    #print(string)
    #result = generate_all_permutations(string,[], set())
    string= ['']*2*n
    print_parentheses(string, 0, n, 0, 0)
    #print(result)

def print_parentheses(string, pos, n, open, close):
    if close == n:
        print(string)
        return
    else:
        if open > close:
            string[pos] = '}'
            print_parentheses(string, pos+1, n, open, close+1)
        if open < n:
            string[pos] = '{'
            print_parentheses(string, pos+1, n, open+1, close)




def validate_string(string):
    stack = []
    for s in string:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
    if len(stack) == 0:
        return True
    return False

def generate_all_permutations(string, path, result_set):
    global count
    if not string and validate_string(path):	
        print(path)
        result_set.add(''.join(path))
        count += 1

    for i in range(len(string)):
        generate_all_permutations(string[:i] + string[i+1:], path + [string[i]], result_set)
    return result_set
generate_parentheses(3)
#print(validate_string('(((()))'))
print(count)

