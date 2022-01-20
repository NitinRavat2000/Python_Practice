class Car:
    wheels = 4              # class(static) variable

    def __init__(self):
        self.mil=10         # instance variable
        self.com="BMW"      # instance variable


c1=Car()   # creatin a object
c2=Car()

Car.wheels=5    # change a value of class variables


print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)