
# inserting and removing values in linkedlist


class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class double_linked_list:

    def __init__(self):
        self.head = None

    def forward(self):

        if self.head is None:
            print("EMPTY")
            return
        
        itr = self.head
        list = ''
        while itr:
            list += str(itr.data) + '--->'
            itr = itr.next
        print("forward",list)

    def backward(self):

        if self.head is None:
            print("EMPTY")
            return
        
        last = self.last_node()
        itr = last
        list = ''
        while itr:
            list += itr.data + '--->'
            itr = itr.prev
        print("backward",list)

    def last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = double_linked_list()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.forward()
    ll.backward()
    ll.insert_at_end("figs")
    ll.forward()
    ll.insert_at(0,"jackfruit")
    ll.forward()
    ll.insert_at(6,"dates")
    ll.forward()
    ll.insert_at(2,"kiwi")
    ll.forward()
