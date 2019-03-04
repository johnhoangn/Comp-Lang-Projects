# I have not received unauthorized aid on this assignment.
# I understand the answers that I have submitted.
# The answers submitted have not been directly copied from another source,
#   but instead are written in my own words.


# [redacted]
# [redacted]
# [redacted]


from Stack import Stack


# handles calculation
def operate(stack, char):
    if char == '!':
        val = not stack.pop()
    elif char == '&':
        val = stack.pop() and stack.pop()
    elif char == '|':
        val = stack.pop() or stack.pop()
    elif char == '=':
        val = stack.pop() is stack.pop()
    elif char == '/':
        val = stack.pop() is not stack.pop()
    else:
        return None

    return val


# driver function
def LogicalEval(input_str):
    stack = Stack()
    for char in input_str:
        val = operate(stack, char)
        if val:
            stack.push(val)
        else:
            stack.push(True if char == '1' else False)

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
