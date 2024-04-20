class StackNode:
    
    def __init__(self, value):
        self.value = value 
        self.next = None
    
    def __str__(self) -> str:
        return f'{self.value} -> {self.next}'


class Stack:
    
    def __init__(self):
        self.top = None
        self.min = None

    def __str__(self) -> str:
        return str(self.top)
    
    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        n = self.top
        min = n.value  
        while n is not None:
            if min > n.value:
                min = n.value
            n = n.next
        self.min = min
        return value

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top 
        self.top = new_node
        if self.min is None:
            self.min = value
        elif value < self.min:
            self.min = value 

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def min(self):
        return self.min 

def test_stack_str():
    stack = Stack()
    assert str(stack) == 'None'
    stack.push(5)
    stack.push(7)
    assert str(stack) == '7 -> 5 -> None'


def test_min():
    stack = Stack() 
    stack.push(3)
    stack.push(5)
    assert stack.min == 3
    stack.push(1)
    assert stack.min == 1
    stack.pop() 
    assert stack.min == 3
    

test_stack_str()
test_min()