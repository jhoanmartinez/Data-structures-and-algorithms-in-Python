"""Para trees perfectos? """
class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_algorithm(start):
    if start is None:
        return
    queue = Queue()
    queue.enqueue(start)
    traversal = ""
    while len(queue) > 0:
        traversal += str(queue.peek()) + "-"
        node = queue.dequeue()
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return traversal


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

print(bfs_algorithm(root))
