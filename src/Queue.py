from Linkedlist import LinkedList
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, data):
        self.linked_list.addLast(data)

    def dequeue(self):
        removed_node = self.linked_list.removeFirst()
        if removed_node:
            return removed_node.data
        else:
            return None

    def isEmpty(self):
        return self.linked_list.head is None