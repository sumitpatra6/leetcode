def decode_string(s):
    stack = []
    integers = ['0','1','2','3','4','5','6','7','8','9']
    for c in s:
        if c == ']':
            current_string = ''
            char = stack.pop()
            while char != '[' and len(stack) > 0:
                current_string = char + current_string
                char = stack.pop()
            mul = ''
            while len(stack)>0 and stack[-1] in integers:
                mul = stack.pop() + mul
            mul = int(mul)
            stack.append(current_string*mul)
        else:
            stack.append(c)
    ret_str = ''
    while len(stack) > 0:
        ret_str = stack.pop() + ret_str
    print(ret_str)
    return ret_str


test1 = '1[a]'
test2 = '3[a2[c]]'
test3 = '2[abc]3[cd]ef'
decode_string(test1)