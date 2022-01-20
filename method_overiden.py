class A:
    def show(self):
        print("in sow A")


class B(A):
    def show(self):
        print("in show B")


c1=B()
c1.show()