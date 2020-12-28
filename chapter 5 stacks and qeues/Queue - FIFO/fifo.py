class Node:
    def __init__(self,dataBox):
        self.data = dataBox
        self.next = None
        self.size = 0

class StackFifo:
    def __init__(self):
        self.head = None

    def enqueue(self, dataNode ):
        new_node = Node(dataNode)
        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            while True:
                if actual_node.next is None:
                    break
                else:
                    actual_node = actual_node.next
            actual_node.next = new_node

    def dequeue(self):
        if self.head is None:
            self.head = None
        else:
            self.head = self.head.next

    def traverse(self):
        if self.head is None:
            print("Empty stack")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node is None:
                    break
                else:
                    print(current_node.data,"--->",current_node.next)
                    current_node = current_node.next

stack = StackFifo()
stack.enqueue("1.kira")
stack.enqueue("2.milo")
stack.enqueue("3.merry")
stack.traverse()
print("*"*80)
stack.dequeue()
stack.traverse()
print("*"*80)
stack.dequeue()
stack.traverse()
print("*"*80)
stack.dequeue()
stack.traverse()
