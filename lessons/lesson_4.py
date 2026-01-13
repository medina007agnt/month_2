"""абстаркция"""
from abc import ABC, abstractmethod

#абстаркный
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

#конкретный
class Dog(Animal):
    def make_sound(self):    #реализация абстракного кода
        print("Гав Гав")

class Cat(Animal):
    def make_sound(self):    #реализация абстракного кода
        print("Мяу Мяу")
puppy = Dog()
puppy.make_sound()
kitty = Cat()
kitty.make_sound()