

class Example:

    def __init__(self,name,age):                 # creating a instance variables
        self.name=name
        self.age=age



    def demo1(self):
        print("first is ",self.name,self.age)

    def demo2(self):
        print("second is ",self.name,self.age)

obj1=Example('nitin',18)
obj2=Example('ketan',21)

obj1.demo1()
obj2.demo2()
