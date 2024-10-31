from abc import ABC, abstractmethod
class Vehicle(ABC):

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Vivo(Vehicle):
    wheels = 4
    def __init__(self, name, year, owner):
        super().__init__(name, year)
        self.owner = owner

    def start(self):
        print(f"{self.name} is running")
        return self

    def stop(self):
        print(f"{self.name} is stopped")
        return self

    def brake(self):
        print('You step on the brakes')
        return self




