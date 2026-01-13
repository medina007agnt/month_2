class User:
    user_count = 0
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        User.user_count += 1
uaer_1 = User("Albert", "996777330232")
print(User.user_count)
User.user_count += 1
print(User.user_count)
