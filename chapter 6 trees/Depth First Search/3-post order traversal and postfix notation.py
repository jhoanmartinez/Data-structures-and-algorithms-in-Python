class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

'#level 0'
root = Node('A')

'#level 1'
root.left = Node('B')
root.right = Node('C')

'#level 2'
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

'#level 3'
root.left.left.left = Node('G')
root.left.left.right = Node('H')
root.right.right.left = Node('I')
root.right.right.right = Node('J')

'#------------------------------------'
'#--------DFS algorithm post order----'
'#------------------------------------'

def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left)
    postorder(current.right)
    print(current.data)
postorder(root)


#page 154
