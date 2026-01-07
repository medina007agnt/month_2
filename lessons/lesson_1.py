class Car:
    #инициализатор __init__ это метод
    def __init__(self, model, color):
        self.model= model
        self.color = color

    def drive_to(self, destination):
        print(f" Car {self.model} Draiving to", destination)

    def change_color(self, new_color):
        self.color = new_color

car_subaru = Car("subaru", "red")
car_toyota = Car("toyota", "whait")
print(car_toyota.model)
print(car_toyota.color)
car_toyota.drive_to("Razzakov")
car_toyota.change_color("black")
print(car_toyota.color)
print(car_subaru.model)
print(car_subaru.color)






