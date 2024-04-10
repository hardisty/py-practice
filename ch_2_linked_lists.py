class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Node = None 

    def __str__(self):
        return f"{self.value} -> {self.next}"
    
    def append_to_tail(self, value: int):
        end = Node(value)
        n = self
        while (n.next is not None):
            n = n.next
        n.next = end


    
    
    

def remove_dupes(ll: Node):
    visited = []
   #n = ll
    while ll is not None and ll.next is not None:
        visited.append(ll.value)
        if ll.next.value in visited:
            ll.next = ll.next.next
        ll = ll.next
    return None

def test_remove_dupes():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    first_len = len(str(head))
    print(head)
    remove_dupes(head)
    print(head)
    assert len(str(head)) < first_len


def remove_dupes_no_buffer(head: Node):
    n = head 
    while n.next is not None:
        if n.value == n.next.value:
            n.next = n.next.next
        elif n.value > n.next.value:
            n.value, n.next.value = n.next.value, n.value
            remove_dupes_no_buffer(head) 
        n = n.next   


def test_remove_dupes_no_buffer():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    first_len = len(str(head))
    print(head)
    remove_dupes_no_buffer(head)
    print(head)
    assert len(str(head)) < first_len


def find(head, k):
    n = head
    counter = 1
    while n.next is not None:
        counter += 1
        n = n.next 
    n = head
    place = counter - k
    counter = 0 

    while place > counter:
        n = n.next 
        counter += 1
    return n.value



def test_find():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    assert find(head, 2) == 5



if __name__ == "__main__":
    test_remove_dupes()
    test_remove_dupes_no_buffer()
    test_find()