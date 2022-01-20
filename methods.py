class Student:

    school="Tapovan"                 # class variable

    def __init__(self,m1,m2,m3):     # instance variables
        self.m1=m1
        self.m2=m2
         self.m3=m3

    def avg(self):                              # Instance method
        return (self.m1+self.m2+self.m3)/3

    @classmethod                                #class method
    def getschool(cls):
        return cls.school

    @staticmethod                       # static method
    def info():
        print("this is studrnt class")



m1=int(input("enterr first mark"))
m2=int(input("enterr second mark"))
m3=int(input("enterr third mark"))

s1=Student(m1,m2,m3)


print(s1.avg())

print(Student.getschool())

Student.info()

