#родительский , суперкласс
class Car:
    def __init__(self, model, color):
        self.model= model
        self.color = color

    def drive_to(self, destination):
        print(f" Car {self.model} Draiving to", destination)

# дочерний , подкласс
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(model,color)
        self.number = number

    def drive_to(self, destination):
        print(f"Bus {self.model} Draiving to", destination)
bus_42 = Bus("Ikareus", "green","42")
print(bus_42.number)
bus_42.drive_to("Bishkek")
print(type(bus_42))
print(isinstance(bus_42, Bus ))  #isinstance — это функция, которая проверяет тип переменной.