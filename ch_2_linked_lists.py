class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Node = None 

    def __str__(self):
        return f"{self.value} -> {self.next}"
    
    
    

def remove_dupes(ll):
    print(ll)
    return None

if __name__ == "__main__":
    ll = Node(5)
    next = Node(6)
    ll.next = next
    print(ll)
    print(ll.next)
    remove_dupes(ll)