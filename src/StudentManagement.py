from BST import BinarySearchTree
from Student import Student

class StudentTree(BinarySearchTree):
  def __init__(self):
    super().__init__()

  def addStudent(self, student):
        self.insert(student)

  def removeStudent(self, id):
        student = self.search(id)
        if student is None:
            print("Student not found")
            return
        self.remove(student)
    
  def updateStudent(self, student):
        self.update(student)

  def viewStudentInorder(self):
        self.printInOrder()

  def displayAllStudent(self):
      if self.root is None:
          print("Student's Tree is empty!!!")
          return
      else:
        print(f"{'ID':<10}|{'Name':<20}|{'Date of Birth':<20}|{'Mark':<5}")
        return self.breadth()
  
  #chua xu ly input
  def searchStudentById(self):
        id = int(input("Enter ID to search: "))
        if self.search(id) is None:
            print("This student id is not exist")
            return
        else: 
            return self.search(id).display() 

  def searchStudentByName(self, name):
        list_student = self.searchByName(name)
        for student in list_student:
            student.display()  
            
  def searchStudentByMark(self, mark):
        list_student = self.searchByMark(mark)
        for student in list_student:
            student.display()    

  #Xu ly file

  def serialize(self, node, file):
    if node is not None:
      file.write(f"{node.data.id},{node.data.name},{node.data.birth},{node.data.mark}\n")
      self.serialize(node.left, file)
      self.serialize(node.right, file)

  def writeToFile(self, filename):
    with open(filename, 'w') as file:
      self.serialize(self.root, file)
  
  def deserialize(self, file):
    lines = file.readlines() #doc tat ca cac dong trong file
    for line in lines:
      id, name, birth, mark = line.strip().split(',')
      self.insert(Student(int(id), name, birth, float(mark)))

  def loadFromFile(self, filename):
    with open(filename, 'r') as file:
      self.deserialize(file)


# test = StudentTree()
# test.loadFromFile('students.txt')
# test.searchStudentById()

