class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()


    def show(self):

        print(self.name,self.rollno)
        self.lap.show()



    class Laptop:

        def __init__(self):
            self.brand="hP"
            self.cpu="i5"
            self.ram="8gb"

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("Nitin",34)
s2=Student("Rahul",45)

s1.show()



