from collections import namedtuple
User = namedtuple("User", ["id", "name", "age"])
user_3 = User(125, "Oleg", 34)
print(user_3)
print(user_3.id)

class User:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return f"{self.name}\n{self.id}\n{self.age}"
        
    def __repr__(self):
        return f"{self.name}\n{self.id}\n{self.age}"        
    def __eq__(self, other):
        return self.name == other.name and self.id == other.id and self.age == other.age
        
user_1 = User("Tom", 123, 31)
user_2 = User("Tom", 123, 31)
print(user_1)
print(user_1 == user_2)
