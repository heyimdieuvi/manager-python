from StudentManagement import StudentManagement
from Student import Student

studentManagement = StudentManagement()

def menu():
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Update a student")
    print("4. View list of students")
    print("5. Search student by ID")
    print("6. Search student by name")
    print("7. Search student by mark")
    print("Your option: ")
    option = int(input())
    
    if option == 1: 
        id = int(input("Enter ID: "))
        name = input("Enter Name:")
        birth = input("Enter year of birth: ")
        mark = float(input("Enter mark: "))
        student = Student(id, name, birth, mark)
        
        studentManagement.addStudent(student)
    elif option == 2:
        id = int(input("Enter ID: "))
        studentManagement.removeStudent(id)
    elif option == 3:
        id = int(input("Enter ID: "))
        name = input("Enter Name:")
        birth = input("Enter year of birth: ")
        mark = float(input("Enter mark: "))
        student = Student(id, name, birth, mark)
        
        studentManagement.updateStudent(student)
    elif option == 4:
        studentManagement.viewStudent()
    elif option == 5:
        id = int(input("Enter ID: "))
        studentManagement.searchStudentById()
    elif option == 6:
        name = input("Enter Name: ")
        studentManagement.searchStudentByName()
    elif option == 7:
        mark = float(input("Enter Mark: "))
        studentManagement.searchStudentByMark()
    else:
        print("Invalid option")
        
        

if __name__ == "__main__":
    while True:
        menu()