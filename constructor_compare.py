class computer:

    def __init__(self):
        self.name="Nitin"
        self.age=21

    def update(self):
        self.age=23

    def compare(self,other):   # compare ages function
        if self.age==other.age:
            print("There ara same")
        else:
            print("there are different")



c1=computer()
c2=computer()




c1.compare(c2)   # compare ages of both objects


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)