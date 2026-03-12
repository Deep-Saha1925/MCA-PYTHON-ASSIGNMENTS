class Father:
    a = 10
    def skill(self): 
        print("Father: Engineering skill")
        
class Mother:
    a = 20
    def skill(self): 
        print("Mother: Art skill")
        
class Child(Mother, Father):
    def info(self):
        print("Child..")
        
c = Child()
c.skill()
c.info()
print(c.a)
print(Child.__mro__)