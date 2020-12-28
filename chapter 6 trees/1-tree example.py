class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#se crean los nodos
n1 = Node("1.Root")
n2 = Node("2.left")
n3 = Node("3.right")
n4 = Node("4.child-left")

#conexion de nodos
n1.left = n2
n1.right = n3
n2.left = n4

#se imprimen los nodos
current_node = n1
while current_node is not None:
    print(current_node.data)
    current_node = current_node.left
