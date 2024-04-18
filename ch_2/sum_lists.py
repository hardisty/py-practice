
class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node = None

    def __str__(self):
        return f"{self.value} -> {self.next}"

    def append_to_tail(self, value: int):
        tail = Node(value)
        n: Node = self
        while n.next is not None:
            n = n.next 
        n.next = tail 



def sum_lists(first: Node, second: Node) -> Node:
    next_carry = 0
    sum_node = None
    while first is not None or second is not None:
        digit = first.value + second.value
        print(f"first: {first}, second: {second}, digit: {digit}")
        curr_carry = next_carry
        if digit >= 10:
            next_carry = 1
            digit -= 10
        else:
            next_carry = 0
        if sum_node is None:
            sum_node = Node(digit + curr_carry)
        else:
            sum_node.append_to_tail(digit + curr_carry)

        if first is not None:
            first = first.next 
        if second is not None:
            second = second.next 
        if first is None and second is None and next_carry == 1:
            sum_node.append_to_tail(1)
    return sum_node


def sum_lists_recursive(first: Node, second: Node) -> Node:
    sum_val = first.value + second.value
    carry = 0 
    if sum_val >= 10:
        carry = 1 
        sum_val -= 10    
    
    sum_node = Node(sum_val)
    
    if first.next is not None and second.next is not None:
        first.next.value += carry
        sum_node.next = sum_lists_recursive(first.next, second.next)
    elif first.next is not None and second.next is None:
        sum_node.next = sum_lists_recursive(first.next, Node(carry))
    elif first.next is None and second.next is not None:
        sum_node.next = sum_lists_recursive(Node(carry), second.next)
    elif first.next is None and second.next is None and carry:
        sum_node.next = Node(1)
    return sum_node

if __name__ == "__main__":


    # 437 + 126 = 5531
    first = Node(4)
    first.append_to_tail(3)
    first.append_to_tail(7)

    second = Node(7)
    second.append_to_tail(2)
    second.append_to_tail(6)
    
    sum_node = sum_lists(first, second)
    print(sum_node)

    sum_node = sum_lists_recursive(first, second)
    print(sum_node)

    print("All done!")