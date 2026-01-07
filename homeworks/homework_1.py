class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


    def introduce(self):
        if self.higher_education:
            education = "у меня высшее образование"
        else:
            education = "у меня нет высшего образрвания"
        print(f"меня зовут {self.name}, я родился(ась) {self.birth_date}, "
              f"по профессии {self.occupation}, {education}")

person1= Person("Медина","20.11.2007", "програмист",True)
person2= Person("Айбек","10.1.2004", "разработчик",False)
person3= Person("Арууке","22.08.2000", "учитель",True)


person1.introduce()
person2.introduce()
person3.introduce()

