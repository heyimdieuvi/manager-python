class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addLast(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def removeFirst(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def deleteByIndex(self, index):
        if index == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
            return
        current = self.head 
        i = 1
        while current is not None and i < index - 1:
            current = current.next
            i += 1
        if current is None or current.next is None:
            return
        temp = current.next
        current.next = temp.next
        temp = None

    def deleteByData(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            temp = None
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next

    def update(self, index, new_data):
        current = self.head
        i = 1
        while current is not None:
            if i == index:
                current.data = new_data
                return
            current = current.next
            i += 1
