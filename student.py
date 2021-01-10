class Student:
    def __init__(self,first,last,cgpa):
        self.first = first
        self.last = last
        self.cgpa = cgpa
        self.email= self.last +"_"+self.first+"@cb.amrita.edu"
    def getFullName(self):
        return self.first+" "+self.last
std1= Student('Fidelis','Akilan',9.0)
std2 = Student('Solar','Claw',8.0)
print(std1.getFullName())    
print(std2.getFullName())    
