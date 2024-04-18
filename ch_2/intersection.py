class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None 

    def __str__(self):
        return f'{self.value} -> {self.next}'
    

def intersection(first: Node, second: Node) -> Node:

    # double nested loop has O(n) squared runtime
    second_head = second
    while first is not None:
        while second is not None:
            if first == second:
                return first
            second = second.next 
        first = first.next
        second = second_head

    return None 

def test_intersection():
    first = Node(3)
    second = Node(42)
    third = Node(5)
    fourth = Node(7)
    fifth = Node(3)

    # object (not value) equality
    assert first == first 
    assert first != fifth

    first.next = second 
    third.next = second 
    fourth.next = third 

    assert intersection(first, third) == second
    assert intersection(first, fifth) is None

if __name__ == '__main__':
    test_intersection()
