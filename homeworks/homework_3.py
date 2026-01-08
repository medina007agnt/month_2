class Person:
    def __init__(self, name, occupation,higher_education):
        self.name = name
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def edu(self):
        if self.__higher_education:
            return "есть"
        else:
            return "нет"

class Classmate(Person):
    def __init__(self,name,occupation, higher_education,group):
        super().__init__(name,occupation,higher_education)
        self.group = group

    def introduce(self):
        print(f"Привет, меня зовут {self.name}.Моя профессия {self.occupation}."
              f" Я учился с Айсулуу в группе {self.group}."
              f"У меня {self.edu()} высшее образование.")


class Friend(Person):
    def __init__(self,name,occupation,higher_education, hobby):
        super().__init__(name,occupation,higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}."
              f" Моя профессия {self.occupation}. Моё хобби {self.hobby}. "
              f"У меня {self.edu()} высшее образование.")

cl1 = Classmate("Иван", "студент",  True,"11D")
fr1 = Friend("Айбек", "студент",  True, "футбол")

cl1.introduce()
fr1.introduce()


