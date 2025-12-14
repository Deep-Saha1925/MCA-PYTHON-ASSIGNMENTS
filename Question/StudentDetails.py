class Student:
    def __init__(self):
        self.roll = int(input("Enter roll: "))
        self.name = input("Enter name: ")
        
    def setMarks(self):
        self.marks = []
        print("Enter marks for Maths, Python, Java, DSA, Computer Network")
        for i in range(5):
            self.marks.append(int(input("Enter marks: ")))
            
    def getStream(self):
        self.stream = input("Enter Stream: A for Arts, C for Commerce, S for Science: ")
        
    def getPercentage(self):
        print("Percentage: ", sum(self.marks)/5)
        
    def calculateGrade(self, marks):
        if marks >= 90:
            return "O"
        elif marks >= 80:
            return "E"
        elif marks >= 70:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
        
    
    def calculateDivision(self, marks):
        if marks >= 60:
            return "1st"
        elif marks >= 50:
            return "2nd"
        elif marks >= 40:
            return "3rd"
        else:
            return "FAIL"
        
        
    def generateGrade(self):
        subs = ['Maths', 'Python', 'Java', 'DSA', 'Computer Network']
        print("\n\n==============GRADE====================")
        for i in range(5):
            mark = self.marks[i]
            print("Subject:", subs[i], "Grade:", self.calculateGrade(mark))
            
    def generateDivision(self):
        subs = ['Maths', 'Python', 'Java', 'DSA', 'Computer Network']
        print("\n\n==============DIVISION=================")
        for i in range(5):
            mark = self.marks[i]
            print("Subject:", subs[i], "Division:", self.calculateDivision(mark))
            
s1 = Student()
s1.getStream()
s1.setMarks()
s1.getPercentage()
s1.generateGrade()
s1.generateDivision()