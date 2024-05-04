from StudentManagement import StudentTree
from HandleInput import Validation

class Menu:
  def __init__(self):
      self.studentManagement = StudentTree()

  def menu(self):
        self.studentManagement.loadFromFile("manager-python\data\students.txt")
        while True:
            print("*----------------------MENU----------------------*")
            print("|    0. Exit                                     |")
            print("|    1. Add a student                            |")
            print("|    2. Remove a student                         |")
            print("|    3. Update a student                         |")
            print("|    4. View list of students                    |")
            print("|    5. View list of students (In Order by ID)   |")            
            print("|    6. Search student by ID                     |")
            print("|    7. Search student by name                   |")
            print("|    8. Search student by mark                   |")
            print("*------------------------------------------------*")

            option = Validation.getInt("Enter your option: ", 0, 7)

            print("__________________________________________________________") 
            if option == 1: 
                self.studentManagement.addStudent()

            elif option == 2:
                self.studentManagement.remove()
                
            elif option == 3:
                self.studentManagement.update()
                
            elif option == 4:
                self.studentManagement.displayAllStudent()

            elif option == 5:
                self.studentManagement.viewStudentInorder()

            elif option == 6:
                self.studentManagement.searchStudentById()

            elif option == 7:
                self.studentManagement.searchByName()

            elif option == 8:
                self.studentManagement.searchByMark()
             
            elif option == 0:
                print("Goodbye ")
                self.studentManagement.writeToFile("manager-python\data\students.txt")
                break
    