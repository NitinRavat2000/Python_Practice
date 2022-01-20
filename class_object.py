

class Example:
    def demo1(self):
        print("Hello Users !")

    def demo2(self):
        print("do some fun")

obj1=Example()
obj2=Example()


Example.demo1(obj1)
Example.demo2(obj2)


obj1.demo1()
obj2.demo2()
