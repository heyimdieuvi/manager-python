class Student:
    def __init__(self, id, name, birth, mark):
        self.id = id
        self.name = name
        self.birth = birth
        self.mark = mark

    def display(self):
        print(f"{self.id:<10}|{self.name:<20}|{self.birth:<20}|{self.mark:<5}") 
    








