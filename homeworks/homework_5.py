class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car starting")

class Tesla(Car, Vehicle):
    def start(self):
        super().start()
        print("Tesla ready")

print(Tesla.__mro__)
tesla = Tesla()
tesla.start()
