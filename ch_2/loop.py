class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value} -> '
    

def find_loop(n: Node):
    node_ids = []
    while n is not None:
        if id(n) in node_ids:
            return n
        node_ids.append(id(n))
        n = n.next

    return None


def test_find_loop():
    first = Node(5)
    second = Node(7)
    third = Node(42)

    first.next = second 
    second.next = third 
    third.next = second 
    
    assert find_loop(first) == second
    assert find_loop(second) == second


if __name__ == '__main__':
    test_find_loop()