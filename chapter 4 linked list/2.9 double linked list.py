
#-------------------------------------------------------------------

# class Node:
#     def __init__(self,data="A"):
#         self.data = data
#         self.prev = None
#         self.next = None

# class doubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
#     def addNode(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = self.head
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
            

#        def traverseList(self):
#            self.count = 0
#            if self.head is None:
#                print("Empty list")
#            else:
#                current_node = self.head
#                while current_node is not None:
#                    if current_node is None:
#                        break
#                    else:
#                        self.count = self.count + 1
#                        print(self.count, ".", current_node.data)
#                        current_node = current_node.next

# double = doubleLinkedList()
# double.addNode("A")
# double.addNode("B")
# double.addNode("C")
# double.traverseList()

class Node:
    def __init__(self,data):
        self.data = data
        self.next, self.prev = None, None

class doubleLinkedList:
    def __init__(self):
        self.head, self.tail = None, None
    
    def addNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def traverseList(self):
        self.count = 0
        if self.head is None:
            print("Empty list")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node is None:
                    break
                else:
                    self.count = self.count + 1
                    print(self.count, ".", current_node.data)
                    current_node = current_node.next

double = doubleLinkedList()
double.addNode("A")
double.addNode("B")
double.addNode("C")
double.addNode("D")
double.traverseList()