class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def deleteByIndex(self, index):
        current = self.head 
        i = 1
        while current is not None:
            if i == index - 1 :
                temp = current.next
                current.next = temp.next
                temp = None
                break
            current = current.next
            i += 1

    def deleteByData(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
            current = None
            return
        else:
            while current is not None:
                if current.next.data == data:
                    temp = current.next
                    current.next = temp.next
                    temp = None
                    break
                current = current.next

    def update(self, index, new_data):
        current = self.head
        i = 1
        while current is not None:
            if i == index:
                current.data = new_data
                break
            current = current.next
            i += 1