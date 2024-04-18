

class Node:

    def __init__(self, value):
        self.value = value 
        self.next = None
        
    def __str__(self):
        return f"{self.value} -> {self.next}"
    
    

def is_palendrome(n: Node) -> bool:

    # build linked list with opposite order
    head = n
    new_head = None
    new_next = None
    while not n is None:
        new_head = Node(n.value)
        new_head.next = new_next
        new_next = new_head
        n = n.next
    
    all_match = True 
    n = head 
    new_n = new_head
    while not n is None:
        if n.value != new_n.value:
            all_match = False
        n = n.next 
        new_n = new_n.next 

    return all_match


def test_is_palendrome():
    first = Node(5)
    second = Node(42)
    first.next = second
    third = Node(5)
    second.next = third 

    assert is_palendrome(first) == True 
    assert is_palendrome(second) == False

if __name__ == "__main__":

    test_is_palendrome()
    print("all done!")