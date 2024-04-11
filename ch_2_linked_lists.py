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
    assert find(head, 3) == 4


def depth(node: Node, decent: int):
    if node.next is None:
        return 1
    else:
        decent += 1
        return depth(node.next, decent) + 1


def test_depth():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    assert depth(head, 0) == 4


def find_recursive(node: Node, k: int, decent: int): # -> (depth, kth)
    if node.next is None:
        return (1, node.value)
    else:
        decent += 1 
        next_depth, next_val = find_recursive(node.next, k, decent)
        curr_depth = next_depth + 1
        total_depth = decent + curr_depth
        print(f"{node}, k: {k}, decent: {decent}, curr_depth: {curr_depth}, next_depth: {next_depth}, next_val: {next_val}")
        if (total_depth - decent) > k:
            return curr_depth, node.next.value
        

def test_find_recursive():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    answer = find_recursive(head, 1, 0)
    print(answer)
    assert answer[1] == 3
    answer = find_recursive(head, 2, 0)
    print(answer)
    assert answer[1] == 5

def delete_middle_node(n: Node):
    if n.next is None:
        n = None
    else:
        while n.next is not None:
            n.value = n.next.value
            n.next = n.next.next 
            n = n.next 
                
def test_delete_middle_node():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    print(head)
    delete_middle_node(head.next)
    print(head)


def partition(n: Node, partition: int):
    # do we need to preserve object identities? assume no
    # let's try to do this in one traversal 
    first_new_head = None
    first_new_tail = None
    second_new_head = None
    while n is not None:
        if n.value < partition:
            if first_new_head is None:
                first_new_head = Node(n.value)
                first_new_tail = first_new_head
            else:
                new_node = Node(n.value)
                new_node.next = first_new_head
                first_new_head = new_node
        else:
            if second_new_head is None:
                second_new_head = Node(n.value)
            else:
                new_node = Node(n.value)
                new_node.next = second_new_head
                second_new_head = new_node 
        n = n.next

    first_new_tail.next = second_new_head
    return first_new_head

def test_partition():
    head = Node(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    head.append_to_tail(3)
    partitioned = partition(head, 4)
    print(partitioned)



if __name__ == "__main__":
    test_remove_dupes()
    test_remove_dupes_no_buffer()
    test_find()
    test_depth()
    # test_find_recursive() doesn't work
    test_delete_middle_node()
    test_partition()
