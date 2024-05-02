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
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def _search(self, data, node):
        if node is None:
            return None
        if data == node.data.id:
            return node.data
        if data < node.data.id:
            return self._search(data, node.left)
        if data > node.data.id:
            return self._search(data, node.right)
        return None

    def search(self, data):
        return self._search(data, self.root)

    def _searchByName(self, data, node, result):
        if node is not None:
            self._searchByName(data, node.left, result)
            self._searchByName(data, node.right, result)
            if data in node.data.name:
                result.append(node.data)
        return result

    def searchByName(self, data):
        return self._searchByName(data, self.root, [])

    def _searchByMark(self, data, node, result):
        if node is not None:
            self._searchByMark(data, node.left, result)
            self._searchByMark(data, node.right, result)
            if data == node.data.mark:
                result.append(node.data)
        return result

    def searchByMark(self, data):
        return self._searchByMark(data, self.root, [])

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
            print(node.data)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def remove(self, data):
        self.root = self._remove_recursive(self.root, data)

    def _remove_recursive(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._remove_recursive(node.left, data)
        if data > node.data:
            node.right = self._remove_recursive(node.right, data)
        if data == node.data:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._remove_recursive(node.right, min_node.data)

        return node

    def _find_min(self, node):
        if node.left is None:
            return node
        return self._find_min(node.left)

    def update(self, data):
        self.root = self._update_recursive(self.root, data)

    def _update_recursive(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self._update_recursive(node.left, data)
        if data > node.data:
            node.right = self._update_recursive(node.right, data)
        if data == node.data:
            node.data = data
            node.left = self._update_recursive(node.left, data)
            node.right = self._update_recursive(node.right, data)
        return node
