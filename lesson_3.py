"""ПОЛИМОРФИЗМ"""
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
        super().drive_to(destination)
        print(f"Bus {self.model} Draiving to", destination)

class Truck(Car):
    def drive_to(self, destination):
        print(f"Truck Draiving to", destination)

bus_42 = Bus("Ikareus", "green","42")
truck = Truck("MAN", "white")
car_subaru = Car("subaru", "red")

vehicales = (bus_42, truck, car_subaru)
for v in vehicales:
    v.drive_to("Bishkek")