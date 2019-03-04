class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def push(self, value):
        self.num_elements += 1
        new_node = LLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def pop(self):
        assert self.size() > 0, "Underflow exception"
        self.num_elements -= 1
        ret = self.head.next.data
        self.head.next = self.head.next.next
        return ret

    def peek(self):
        assert self.size() > 0, "Underflow exception"
        return self.head.next.data

    def double_peek(self):
        assert self.size() > 1, "Underflow exception"
        return self.head.next.next.data

    def size(self):
        return self.num_elements

    def print(self):
        cur_node = self.head.next
        print("List size (%d), Contents:" % self.size())
        while cur_node != self.tail:
            print("> %s" % cur_node.data)
            cur_node = cur_node.next

    def __init__(self):
        self.num_elements = 0
        self.tail = LLNode(None)
        self.head = LLNode(None)
        self.head.next = self.tail
