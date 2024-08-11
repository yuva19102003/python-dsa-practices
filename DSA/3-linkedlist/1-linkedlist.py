
# class for nodes which is considered as an element of linked list
# Below is an implementation of this doubly linked list:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    


# creating object

node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
node4 = Node(8)
node5 = Node(10)


node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node5
node4.prev = node3

node5.prev = node4

print("=====================================================")

forward_current = node1

print("traversal forward")

while forward_current:
    print(forward_current.data, end="--->")
    forward_current = forward_current.next

print("null")

print("=====================================================")

print("traversal backward")

backward_current = node5

while backward_current:
    print(backward_current.data, end="--->")
    backward_current = backward_current.prev
print("null")

print("=====================================================")