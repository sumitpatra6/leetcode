class SetOfStacks(object):
    def __init__(self):
        super().__init__()
        self.stacks = [[]]
        self.current_stack_index = 0
        self.threshold = 3
    
    def push(self, data):
        if len(self.stacks[self.current_stack_index]) >= self.threshold:
            self.stacks.append([])
            self.current_stack_index += 1
        self.stacks[self.current_stack_index].append(data)

    def pop(self):
        if len(self.stacks[self.current_stack_index]) == 0 and len(self.stacks) == 1:
            print("Empty stack")
            return
        if len(self.stacks[self.current_stack_index]) == 0:
            self.stacks.pop()
            self.current_stack_index -= 1
        return self.stacks[self.current_stack_index].pop()
    
    def peek(self):
        if len(self.stacks[self.current_stack_index]) == 0 and len(self.stacks) == 1:
            print("Empty stack")
            return
        if len(self.stacks[self.current_stack_index]) == 0:
            self.stacks.pop()
            self.current_stack_index -= 1
        return self.stacks[self.current_stack_index][-1]
    
    def popAtIndex(self, index):
        if index > self.current_stack_index or index < 0:
            print("Invalid index.")
            return
        return self.stacks[index].pop()
        

stack_obj =SetOfStacks()
for i in range(9):
    stack_obj.push(i)

for i in range(10):
    print(stack_obj.pop())
        
print(stack_obj.stacks)

