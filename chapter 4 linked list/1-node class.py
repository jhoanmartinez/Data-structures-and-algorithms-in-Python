class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(data)

n1 = Node("Kira")
n2 = Node("milo")
n3 = Node("spam")

n1.next = n2
n2.next = n3
current = n1

while True:

    print(current.data)
    current = current.next
    if current is None:
        break
