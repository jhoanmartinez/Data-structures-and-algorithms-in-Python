class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insertNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while True:
                if current_node.next is None:
                    break
                else:
                    current_node = current_node.next
            current_node.next = new_node
  
    def printList(self):
        if self.head is None:
            print("Empty list")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node is None:
                    break
                else:
                    print(current_node.data,"--->",current_node.next)
                    current_node = current_node.next                

list = linkedlist()
list.printList()
print("*"*80)
list.insertNode("Kira")
list.insertNode("Milo")
list.insertNode("Merry")
list.printList()
    
