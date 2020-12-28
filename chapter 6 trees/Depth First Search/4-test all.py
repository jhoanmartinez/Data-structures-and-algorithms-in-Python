class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

'#Level 0'
root = Node("A")

'#level 1'
root.left = Node("B")
root.right = Node("C")

'#level 2'
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

'#level 3'
root.left.left.left = Node("G")
root.left.left.right = Node("H")

# def inorder(root):
#     current = root
#     if current is not None:
#         inorder(current.left)
#         print(current.data)
#         inorder(current.right)
# inorder(root)

# def pre_order(root):
#     current = root
#     if current is not None:
#         print(current.data)
#         pre_order(current.left)
#         pre_order(current.right)
# pre_order(root)

# def post_order(root):
#     current = root
#     if current is not None:
#         post_order(current.left)
#         post_order(current.right)
#         print(current.data)
# post_order(root)
