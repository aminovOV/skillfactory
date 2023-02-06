from cat import Cat


class Dog(Cat):
    def get_pet(self):
        return self.name, self.age


muhtar = Dog("Мухтар", 5)
print(muhtar.get_pet())
