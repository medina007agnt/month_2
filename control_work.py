class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name  = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"Собачка {self.name}, {self.age} годика, издаёт звук 'гав гав'")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
       print(f"Кошка {self.name}, {self.age} годика, издаёт звук 'мяу мяу'")

dog = Dog("Бобик","4")
cat = Cat("Луна","2")

dog.make_sound()
cat.make_sound()



