from Stack import Stack


# handles calculation
def operate(stack, char):
    if char == '!':
        val = not stack.pop()
        return val

    right = stack.pop()
    left = stack.pop()

    if char == '&':
        return left and right
    elif char == '|':
        return left or right
    elif char == '=':
        return left == right
    elif char == '/':
        return left != right


# driver function, input_str must be a valid postfix expression
def LogicalEval(input_str):
    stack = Stack()
    for char in input_str:
        if char == '1' or char == '0':
            stack.push(True if char == '1' else False)
        elif stack.size() > 0:
            stack.push(operate(stack, char))

    # debug
    # stack.print()

    # print method 1
    # print('%s evaluates to %s' % (input_str,  '1' if stack.peek() else '0'))

    # print method 2
    print('1' if stack.peek() else '0')


# tests
LogicalEval('0!!!1/10&1!!&=1=0|')
LogicalEval('10=!10/&11!0/=1|11!&|&0/')
LogicalEval('01=1/10|1/&')
LogicalEval('11=0/0!&1|')
LogicalEval('10&11!&|0/')
