from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.get_name()} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.get_name()} says Meow"

class RobotDog(Dog):
    def speak(self):
        return f"{self.get_name()} says Beep Woof"

animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    RobotDog("Rex")
]

for a in animals:
    print(a.speak())