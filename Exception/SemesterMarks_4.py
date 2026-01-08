class Negativemarks(Exception):
    def __init__(self):
        print("No negative marks!!")
        
class Range(Exception):
    def __init__(self):
        print("Marks should be between 0 and 100!!")
        
class AllMarks(Exception):
    def __init__(self):
        print("All marks should be entered")
        
a = int(input("Enter marks(1st sem): "))
b = int(input("Enter marks(2nd sem): "))
c = int(input("Enter marks(3rd sem): "))
d = int(input("Enter marks(4th sem): "))

try:
    if a<0 or b<0 or c<0 or d<0:
        raise Negativemarks
    if a<0 or a>100 or b<0 or b>100 or c<0 or c>100 or d<0 or d>100:
        raise Range
    if a == None or b == None or c == None or d == None:
        raise AllMarks
    else:
        print("Average:", (a+b+c+d)/4)
except Negativemarks:
    pass
except Range:
    pass
except AllMarks:
    pass