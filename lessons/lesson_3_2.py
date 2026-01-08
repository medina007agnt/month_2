"""инкапсуляция"""

class Car:
    def __init__(self, model, color):
        self.model= model
        self.color = color
        self._fined = False      # одно подчеркивание защищенный protected
        self.__max_speed =0      # два подчеркиваний приватный private
                                 # работают только внутри клааса
    def drive_to(self, destination):
        self._test()
        print(self._fined)
        print(self.__max_speed)
        print(f" Car {self.model} driving to", destination)

    def _test(self):
        print(f"Car {self.color}")
    #геттер - получить
    def get_max_speed(self):
        return self.__max_speed
    #сеттер - выставить
    def set_max_speed(self, value):
        if value <=0:
            raise ValueError("max_speed")
        self.__max_speed = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self,value):
        if value <=0:
            raise ValueError("max_speed")
        self.__max_speed = value


car_subaru = Car("Subaru", "red")
print(car_subaru.color)
car_subaru.drive_to("Bishkek")
print(car_subaru._fined)
# print(car_subaru._Car__max_speed)  (только для тестов)  так можно добраться до приватного атрибута
print(car_subaru.get_max_speed)
car_subaru.set_max_speed(-10)
print(car_subaru.get_max_speed())
