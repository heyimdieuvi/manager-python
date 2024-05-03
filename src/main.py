from StudentManagement import StudentManagement
from Student import Student
from datetime import datetime

studentManagement = StudentManagement()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_date_format(s):
    format = "%d-%m-%Y"
    try:
        datetime.strptime(s, format)
        return True
    except ValueError:
        return False
    
def is_mark(s):
    try:
        if 0 <= float(s) <= 10:
            return True
        else:
            return False
    except ValueError:
        return False 
    
def is_id(s):
    try:
        if 0 <= int(s):
            return True
        else:
            return False
    except ValueError:
            return False

def menu():
    while True:
        print("*----------------MENU-----------------*")
        print("|    0. Exit                          |")
        print("|    1. Add a student                 |")
        print("|    2. Remove a student              |")
        print("|    3. Update a student              |")
        print("|    4. View list of students         |")
        print("|    5. Search student by ID          |")
        print("|    6. Search student by name        |")
        print("|    7. Search student by mark        |")
        print("*-------------------------------------*")
        print("Your option: ", end="")
        option = input() #str
        while not is_number(option):
            print("Invalid option, please enter again: ", end="")
            option = input()
        option = int(option) #str -> int

        print("_______________________________________") 
        if option == 1: 
            print("Enter student information: ")

            id = input("Enter ID: ")
            while not is_id(id):
                print("Invalid ID, please enter again: ")
                id = input()
            id = int(id)

            name = input("Enter Name:")
            birth = input("Enter year of birth: ")
            while not is_date_format(birth):
                print("Invalid date format, please enter again: ", end="")
                birth = input()
        
            mark = input("Enter mark: ")
            while not is_mark(mark):
                print("Invalid mark, please enter again: ", end="")
                mark = input()
            mark = float(mark)
            
            student = Student(id, name, birth, mark)
            
            studentManagement.addStudent(student)
        elif option == 2:
            print("Enter student ID to remove: ")

            id = input("Enter ID: ")
            while not is_id(id):
                print("Invalid ID, please enter again: ")
                id = input()
            id = int(id)
            
            studentManagement.removeStudent(id)
        elif option == 3:
            print("Enter student infomation: ")

            id = input("Enter ID: ")
            while not is_id(id):
                print("Invalid ID, please enter again: ")
                id = input()
            id = int(id)
            
            name = input("Enter Name:")
            birth = input("Enter year of birth: ")
            while not is_date_format(birth):
                print("Invalid date format, please enter again: ", end="")
                birth = input()
        
            
            mark = input("Enter mark: ")
            while not is_mark(mark):
                print("Invalid mark, please enter again: ", end="")
                mark = input()
            mark = float(mark)
            student = Student(id, name, birth, mark)
            
            studentManagement.updateStudent(student)
        elif option == 4:
            print("List of student: ")

            studentManagement.viewStudent()
        elif option == 5:
            print("Enter student ID to search: ")

            id = input("Enter ID: ")
            while not is_number(id):
                print("Invalid ID, please enter again: ", end="")
                id = input()
            id = int(id)
            
            studentManagement.searchStudentById(id)
        elif option == 6:
            print("Enter student name to search: ")

            name = input("Enter Name: ")
            studentManagement.searchStudentByName(name)
        elif option == 7:
            print("Enter student mark to search: ")
            
            mark = input("Enter Mark: ")
            while not is_mark(mark):
                print("Invalid mark, please enter again: ", end="")
                mark = input()
            mark = float(mark)
            studentManagement.searchStudentByMark(mark)
        elif option == 0:
            print("Goodbye ")
            break
    
        else:
            print("Invalid option")
            
        

if __name__ == "__main__":
    menu()