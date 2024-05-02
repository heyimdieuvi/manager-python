from distutils.file_util import write_file
from Linkedlist import LinkedList
from Linkedlist import ListNode
from Student import Student
from Queue import Queue

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data.id < node.data.id:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data.id > node.data.id:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def _search(self, name, node, result):
        if node is not None:
            self._search(name, node.left, result)
            self._search(name, node.right, result)
            if name in node.data.name:
                result.append(node.data)
        return result

    def search(self, name):
        return self._search(name, self.root, [])

    def _inOrder(self, node):
      if node is not None:
        self._inOrder(node.left)
        node.data.display()
        self._inOrder(node.right)

    def printInOrder(self):
      self._inOrder(self.root)
      print()

    def breadth_first_traversal(self):
        if self.root is None:
            return
        
        queue = Queue()  # Sử dụng class Queue đã triển khai
        queue.enqueue(self.root)

        while not queue.isEmpty():
            node = queue.dequeue()
            node.data.display()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


student1 = Student(1, "Alice", "2000-01-01", 10)
student2 = Student(5, "Bob", "2001-05-15", 2)
student3 = Student(4, "Charlie", "1999-11-30", 3)

test = BinarySearchTree()
test.insert(student1)
test.insert(student2)
test.insert(student3)

test.breadth_first_traversal()
