class Person:
    def __init__(self, name, birth_date, occupation, owner_name):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.owner_name = owner_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, родилась {self.birth_date}.Я {self.occupation}")

class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, родился(ась) {self.birth_date}."
              f" Я {self.occupation}, друг {self.owner_name}")

class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, родился(ась) {self.birth_date}."
              f" Я {self.occupation}, одноклассник(ца) {self.owner_name}")


friend = Friend("Алмаз","29.09.2007","программист","Медины")
friend.introduce()

classmate = Classmate("Ираада","1.01.2007","программист","Медины")
classmate.introduce()