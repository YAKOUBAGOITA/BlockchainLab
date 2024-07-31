import hashlib

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class HashDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

    def apply_sha2(self):
        current = self.head
        while current:
            # Convert character array (string) to SHA-256 hash
            sha256_hash = hashlib.sha256(current.data.encode()).hexdigest()
            current.data = sha256_hash
            current = current.next

# Example usage:
dll =HashDoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")

print("Original list (forward):")
dll.display_forward()

print("Original list (backward):")
dll.display_backward()

# Apply SHA-2 hashing to the list data
dll.apply_sha2()

print("Hashed list (forward):")
dll.display_forward()

print("Hashed list (backward):")
dll.display_backward()
