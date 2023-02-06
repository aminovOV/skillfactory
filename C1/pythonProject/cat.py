class Cat:
    def __init__(self, name="", age=1, gender=""):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


class Client:
    def __init__(self, name="", second_name="", city="", balance=0):
        self.name = name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.second_name}. ' \
               f'{self.city}. Баланс: {self.balance} р.'

#     def get_company_party(self, clients_dict):
#         self.name = clients_dict.get("name")
#         self.second_name = clients_dict.get("second_name")
#         self.city = clients_dict.get("city")
#
#
# ivan_petrov = Client('Иван', 'Петров', 'Москва', 50)
# print(ivan_petrov)
# clients = [
#     {"name": "Олег", "second_name": "Аминов", "city": "Ufa"},
#     {"name": "Аминов", "second_name": "Аминов", "city": "Ufa"},
#     {"name": "Нелли", "second_name": "Рахматуллина", "city": "Ufa"},
# ]
# for client in clients:
#     client_obj = Client()
#     client_obj.get_company_party(client)
#     print(f'Имя: {client_obj.name}, Фамилия: {client_obj.second_name}, '
#           f'Город: {client_obj.city}')

    def get_company_party(self):
        return f'{self.name}, {self.second_name}, {self.city}'


client_1 = Client("Олег", "Аминов", "Ufa", 50)
client_2 = Client("Олег", "Аминов", "Ufa", 50)
client_3 = Client("Рахматуллина", "Нелли", "Ufa", 50)
clients_list = [client_1, client_2, client_3]
for client in clients_list:
    print(client.get_company_party())
