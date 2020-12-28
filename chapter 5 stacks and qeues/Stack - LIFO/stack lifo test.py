class Node:
    def __init__(self, info):
        self.data = info
        self.next = None

class StackLifo:
    def __init__(self):
        self.head = None
        self.size = 0

    def pushNode(self, dataNode):
        new_node = Node(dataNode)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def traverse(self):
        if self.head is None:
            print("empty stack")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node is None:
                    break
                else:
                    print(current_node.data,"--->",current_node.next)
                    current_node = current_node.next

stack = StackLifo()
stack.pushNode("1.kira")
stack.pushNode("2.milo")
stack.pushNode("3.merry")
stack.traverse()
