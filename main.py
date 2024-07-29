
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if(isEmpty(stack)):
        return 'stack is already empty'

    return stack.pop(0)

def peek(stack):
    if(isEmpty(stack)):
        return 'stack is empty'

    return stack[len(stack) - 1]



stack = createStack()
push(stack, 10)
push(stack, 2)
push(stack, 3)
push(stack, 4)

print(stack)
print(peek(stack))
print(pop(stack))
print(stack)
