class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = [10, 20, 30]
        
    def showData(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        
    def showMarks(self):
        print("Marks:", self.marks)
        
s1 = Student("Deep", 15)
s1.showData()
s1.showMarks()