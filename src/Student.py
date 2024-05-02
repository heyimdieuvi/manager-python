class Student:
    def __init__(self, id, name, birth, mark):
        self.id = id
        self.name = name
        self.birth = birth
        self.mark = mark

    def display(self):
        print(f"{self.id}, {self.name}, {self.birth}, {self.mark}") 
        
    def __eq__(self, other):
        return self.id == other.id
    
    def __lt__(self, other):
        return self.id < other.id
    
    def __gt__(self, other):
        return self.id > other.id
    
    def __le__(self, other):
        return self.id <= other.id
    
    def __ge__(self, other):
        return self.id >= other.id








