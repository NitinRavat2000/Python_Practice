from abc import *


class Computer(ABC):
    @abstractmethod
    def proccess(self):
        pass


class Laptop(Computer):
    def proccess(self):
        print("its running")


class Programmer:
        def work(self,com):
            print("solving bugs")
            com.proccess()


lap=Laptop()


prog1=Programmer()
prog1.work(lap)