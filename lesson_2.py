#родительский , суперкласс
class Car:
    def __init__(self, model, color):
        self.model= model
        self.color = color

    def drive_to(self, destination):
        print(f" Car {self.model} Draiving to", destination)

# дочерний , подкласс
class Bus(Car):
    def drive_to(self, destination):
        print(f"Bus {self.model} Draiving to", destination)
bus_42 = Bus("Ikareus", "green")
print(bus_42)