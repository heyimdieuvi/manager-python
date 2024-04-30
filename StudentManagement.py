import Student
import Linkedlist

class StudentManagement:
    def _init_(self):
        self.list_student = Linkedlist()

    def add_student(self, student):
        self.list_student.append(student)

    def delete_studednt(self, id):
        self.list_student.deleteByData(id)

    def update_student(self, id, student):
        self.list_student.update(id, student)
