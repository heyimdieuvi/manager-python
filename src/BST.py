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
    
    #insert new node with data

    def insert(self, data):
       if self.root is None:
          self.root = TreeNode(data)
       else: self._insert_rec(self.root, data)    
    
    def _insert_rec(self, node, data):
      if data.id < node.data.id:
          if node.left is None:
             node.left = TreeNode(data)
          else: 
             self._insert_rec(node.left, data)
      elif data.id > node.data.id:
          if node.right is None:
             node.right = TreeNode(data)
          else:
             self._insert_rec(node.right, data)
    
    # Tìm kiếm = id

    def _search(self, id, node):
       if id == node.data.id:
          return node.data
       
       if node is not None:
          self._search(id, node.left)
          self._search(id, node.right)


    def search(self, id):
        return self._search(id, self.root).display()

    #inorder display

    def _inOrder(self, node):
      if node is not None:
        self._inOrder(node.left)
        node.data.display()
        self._inOrder(node.right)

    def printInOrder(self):
      self._inOrder(self.root)
      print()

    #breadth first search display

    def breadth(self):
       if self.root is None:
          return
       queue = Queue()
       queue.enqueue(self.root)
       while not queue.isEmpty():
          node = queue.dequeue()
          node.data.display()
          if node.left is not None:
             queue.enqueue(node.left)
          if node.right is not None:
             queue.enqueue(node.right)

    #delete 
    
    #update



