from BST import BinarySearchTree
from Student import Student
from HandleInput import Validation

class StudentTree(BinarySearchTree):
  def __init__(self):
    super().__init__()

  def checkInputID(self):
      check = True
      while check:
          id = Validation.getInt("Enter ID: ", 1, 9999)
          if self.search(id) is None:
              check = False
          else: 
              print("This student's ID is exist.")
      return id

  def addStudent(self):
      id = self.checkInputID()
      name = input("Enter Name: ")
      birth = Validation.getBirth()
      mark = Validation.getFloat("Enter student's mark: ", 0, 10)
      self.insert(Student(id, name, birth, mark))
      print("Add new Student successfully!")

  def removeStudent(self):
        id = Validation.getInt("Enter ID: ", 1, 9999)
        student = self.search(id)
        if student is None:
            print("Student not found")
            return
        self.remove(student)
    
  def updateStudent(self):
        id = Validation.getInt("Enter ID: ", 1, 9999)
        if self.search(id) is None:
            print("Student's ID not found.")
            return
        else:
            name = input("Enter Name: ")
            birth = input("Enter year of birth: ")
            mark = Validation.getFloat("Enter student's mark: ", 0, 10)
            update_student = Student(id, name, birth, mark)
            self.update(update_student)
            print("Update Successfully!!!")

  def viewStudentInorder(self):
        print(f"{'ID':<10}|{'Name':<20}|{'Date of Birth':<20}|{'Mark':<5}") 
        print("----------------------------------------------------------")       
        self.printInOrder()

  def displayAllStudent(self):
      if self.root is None:
          print("Student's Tree is empty!!!")
          return
      else:
        print(f"{'ID':<10}|{'Name':<20}|{'Date of Birth':<20}|{'Mark':<5}")
        print("----------------------------------------------------------") 
        return self.breadth()
  

  def searchStudentById(self):
        id = Validation.getInt("Enter ID: ", 1, 9999)
        if self.search(id) is None:
            print("This student id is not exist")
            return
        else: 
            return self.search(id).display() 

  def searchStudentByName(self):
        name = input("Enter student name to search: ").lower()
        list = self.searchByName(name)
        if len(list) == 0:
            print("Not Found!!!")
            return
        for student in list:
            student.display()
            
  def searchStudentByMark(self):
        mark = Validation.getFloat("Enter student's mark: ", 0, 10)
        list_student = self.searchByMark(mark)
        if len(list_student) == 0:
            print("Not Found!!!") 
            return      
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


