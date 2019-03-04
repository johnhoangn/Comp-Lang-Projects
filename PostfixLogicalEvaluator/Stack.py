# singly linked node
class LLNode:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list implementation of a stack with sentinel nodes
class Stack:
    # push to top
    def push(self, value):
        self.num_elements += 1
        new_node = LLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    # pop from top, size must be > 0
    def pop(self):
        assert self.size() > 0, "Underflow exception"
        self.num_elements -= 1
        ret = self.head.next.data
        self.head.next = self.head.next.next
        return ret

    # look at top, size must be > 0
    def peek(self):
        assert self.size() > 0, "Underflow exception"
        return self.head.next.data

    # get num elements
    def size(self):
        return self.num_elements

    # debug
    def print(self):
        cur_node = self.head.next
        print("List size (%d), Contents:" % self.size())
        while cur_node != self.tail:
            print("> %s" % cur_node.data)
            cur_node = cur_node.next

    # constructor
    def __init__(self):
        self.num_elements = 0
        self.tail = LLNode(None)
        self.head = LLNode(None)
        self.head.next = self.tail
