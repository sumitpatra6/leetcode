def sorted_insertion(element, stack):
    print(stack)
    if len(stack) ==0 :
        stack.append(element)
        return stack
    if stack[-1] > element:
        stack.append(element)
        return stack
    x = stack.pop()
    stack = sorted_insertion(element, stack)
    stack.append(x)
    return stack

def sort_stack(stack):
    temporary_stack = []
    while len(stack) > 0:
        temporary_stack = sorted_insertion(stack.pop(), temporary_stack)

    print(temporary_stack)


sort_stack([1,4,5,3])