def creatStack():
  stack = []
  return stack


def isEmpty(stack):
  return len(stack) == 0


def pop(stack):
  if (isEmpty(stack)):
    return 'Stack is empty'

  return stack.pop()


def push(stack, item):
  return stack.append(item)


def peek(stack):
  if (isEmpty(stack)):
    return 'Stack is empty'

  return stack[len(stack) - 1]


stack = createStack()

push(stack, 10)
push(stack, 2)
push(stack, 3)
push(stack, 4)

print(stack)
print(peek(stack))
print(stack.pop())
print(stack)



`