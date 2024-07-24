class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
       self.head=None
       self.tail=None

    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def __str__(self):
        result=[]
        current = self.head
        while current:
            result.append(str(current.data))
            current=current.next
        return"->".join(result)
linked_list=  SinglyLinkedList()  
linked_list.append("M")
linked_list.append("N")
linked_list.append("K")
linked_list.append("L")

print(linked_list)