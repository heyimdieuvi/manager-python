from BST import BinarySearchTree
from Student import Student


class StudentManagement():
    def __init__(self):
        self.listStudent = BinarySearchTree()

    def addStudent(self, student):
        self.listStudent.insert(student)

    def removeStudent(self, id):
        student = self.listStudent.search(id)
        if student is None:
            print("Student not found")
            return
        self.listStudent.remove(student)

    def updateStudent(self, student):
        self.listStudent.update(student)

    def viewStudent(self):
        self.listStudent.printInOrder()

    def searchStudentById(self, id):
        student = self.listStudent.search(id)
        student.display()

    def searchStudentByName(self, name):
        list_student = self.listStudent.searchByName(name)
        for student in list_student:
            student.display()
            
    def searchStudentByMark(self, mark):
        list_student = self.listStudent.searchByMark(mark)
        for student in list_student:
            student.display()


list1 = StudentManagement()
student1 = Student(1, "A", "2000", 8.0)
student2 = Student(2, "B", "2001", 9.0)
student3 = Student(3, "C", "2002", 7.0)
student4 = Student(4, "D", "2003", 6.0)
student5 = Student(5, "E", "2004", 5.0)
student6 = Student(6, "F", "2005", 4.0)

list1.addStudent(student1)
list1.addStudent(student2)
list1.addStudent(student3)
list1.addStudent(student4)
list1.addStudent(student5)
list1.addStudent(student6)

list1.viewStudent()

print('---------------------------------')
list1.removeStudent(3)
list1.viewStudent()

print('---------------------------------')
list1.updateStudent(Student(2, "BB", "2020", 10))
list1.viewStudent()
print('---------------------------------')

list1.searchStudentById(2)
print('---------------------------------')


list1.searchStudentByName("B")
print('---------------------------------')
list1.searchStudentByMark(8.0)
