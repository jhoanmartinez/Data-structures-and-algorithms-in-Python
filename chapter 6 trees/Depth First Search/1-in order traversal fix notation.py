
# class Node:
#     def __init__(self, dataNode):
#         self.dataNode = dataNode
#         self.right = None
#         self.left = None
#
# root = Node("A")
#
# root.left = Node("B")
# root.right = Node("C")
#
# root.left.left = Node("D")
# root.left.right = Node("E")
# root.right.right = Node("F")
#
# root.left.left.left = Node("G")
# root.left.left.right = Node("H")
#
# def inorder(root):
#     current = root
#     if current is None:
#         return
#     inorder(current.left)
#     print(current.dataNode)
#     inorder(current.right)
#
# print("Tree depth First Search")
# inorder(root)
# ===> G–D-H-B-E-A-C-F.

'#--------------------------------------------------------'
'#------------------------Node class----------------------'
'#--------------------------------------------------------'

class Node:
    def __init__(self, dataNode):
        self.dataNode = dataNode
        self.left = None
        self.right = None

'#--------------------------------------------------------'
'#------------------------Tree----------------------------'
'#--------------------------------------------------------'

# '#level 1'
# root = Node("A")
#
# '#level 2'
# root.left = Node("B")
# root.right = Node("C")
#
# '#level 3'
# root.left.left = Node("D")
# root.left.right = Node("E")
# root.right.right = Node("F")
#
# '#level 4'
# root.left.left.left = Node("G")
# root.left.left.right = Node("H")

'#-----------------------------------------------------'
'#level 1'
root = Node("1")

'#level 2'
root.left = Node("2")
root.right = Node("3")

'#level 3'
root.left.left = Node("4")
root.left.right = Node("5")
root.right.right = Node("6")

'#level 4'
root.left.left.left = Node("7")
root.left.left.right = Node("8")
'#--------------------------------------------------------'
'#------------------------DFS algorithm-------------------'
'#--------------------------------------------------------'

def dfs_inorder(root):
    current_node = root
    if current_node is not None:
        print("searching...")
        dfs_inorder(current_node.left)
        print("DFS node found",current_node.dataNode)
        dfs_inorder(current_node.right)


dfs_inorder(root)

#pag 167
