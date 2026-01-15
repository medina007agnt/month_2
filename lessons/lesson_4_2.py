class User:
    #переменная класса
    user_count = 0
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        User.user_count += 1

    @classmethod
    def get_user_count(cls, name, phone):
        ...
    @classmethod
    def create_user(cls, name, phone):
        new_user = cls(name, phone)
        return new_user

    @staticmethod
    def validate_phone(phone: str)-> bool:
        if phone.isdigit():
            return True
        return False
uaer_1 = User("Albert", "996777330232")
print(User.user_count)
User.user_count += 1
print(User.user_count)
