from BST import BinarySearchTree
from Student import Student

class StudentTree(BinarySearchTree):
  def __init__(self):
    super().__init__()
    
  def addStudent(self):
    id = int(input("Enter ID: "))
    name = input("Enter Name:")
    birth = input("Enter year of birth: ")
    mark = float(input("Enter mark: "))

    student = Student(id, name, birth, mark)
    self.insert(student)
  
  def displayAllStudent(self):
    print(f"{'ID':<10}|{'Name':<20}|{'Date of Birth':<20}|{'Mark':<5}")
    return self.breadth()
  
  def searchByID(self):
    id = int(input("Enter ID that you want to find: "))
    return self.search(id)
  
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


list1 = StudentTree()

# student1 = Student(1, "Alice", "2000-01-01", 10)
# student2 = Student(5, "Bob", "2001-05-15", 2)
# student3 = Student(4, "Charlie", "1999-11-30", 3)
student4 = Student(10, "Vi", "1999-11-30", 10)

test = StudentTree()
test.loadFromFile('students.txt')
# test.insert(student1)
# test.insert(student2)
# test.insert(student3)
test.insert(student4)
test.writeToFile('students.txt')
