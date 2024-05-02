from BST import BinarySearchTree
from Student import Student

class StudentManagement(BinarySearchTree):
  def __init__(self):
    super().__init__()
    
  def addStudent(self):
    id = int(input("Enter ID: "))
    name = input("Enter Name:")
    birth = input("Enter year of birth: ")
    mark = float(input("Enter mark: "))

    student = Student(id, name, birth, mark)
    self.insert(student)

list1 = StudentManagement()

list1.addStudent()
list1.printInOrder()
