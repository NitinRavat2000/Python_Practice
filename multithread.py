from time import *
from threading import *

class A(Thread):
    def run(self):
        for i in range(15):
            print("HEllo")
            sleep(1)

class B(Thread):

    def run(self):
        for i in range(15):
            print("Hii")
            sleep(1)

a=A()
b=B()

a.start()
sleep(0.2)
b.start()

a.join()
b.join()

print("bye")
