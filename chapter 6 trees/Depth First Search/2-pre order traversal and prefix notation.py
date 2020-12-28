class Node:
    def __init__(self, dataNode):
        self.dataNode = dataNode
        self.left = None
        self.right = None

'#level 1'
root = Node("A")

'#level 2'
root.left = Node("B")
root.right = Node("C")

'#level 3'
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

'#level 4'
root.left.left.left = Node("G")
root.left.left.right = Node("H")

'#--------------------------------------------------------'
'#------------------------DFS algorithm-------------------'
'#--------------------------------------------------------'
def preorder(root_node):
    current = root_node
    if current is None:
        print("Searching...")
    else:
        print(current.dataNode)
        preorder(current.left)
        preorder(current.right)

preorder(root)

pag 152
