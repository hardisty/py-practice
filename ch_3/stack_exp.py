class EmptyStackException(LookupError):
    pass

class StackNode:
    
    def __init__(self, value):
        self.value = value 
        self.next = None
    
    def __str__(self) -> str:
        return f'{self.value} -> {self.next}'


class Stack:
    
    def __init__(self):
        self.top = None

    def __str__(self) -> str:
        return str(self.top)
    
    def pop(self):
        if self.top is None:
            raise EmptyStackException('pop on empty Stack')
        value = self.top.value
        self.top = self.top.next 
        return value

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top 
        self.top = new_node

    def peek(self):
        if self.top is None:
            return None
        return self.top.value 

def test_stack_str():
    stack = Stack()
    assert str(stack) == 'None'
    stack.push(5)
    stack.push(7)
    assert str(stack) == '7 -> 5 -> None'

test_stack_str()

print('all done!')