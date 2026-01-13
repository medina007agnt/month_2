class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        phone_str = str(phone_number)
        return phone_str.isdigit() and len(phone_str) == 10

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            print("ОШИБКА: номер телефона должен содержать ровно 10 цифр!")


print(ContactList.all_contacts)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)

ContactList.add_contact("John Doe", "5551234")