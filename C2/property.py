# Задание 2.5.8
# Создайте вычисляемое свойство для класса Square.
#
# Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер.
# В сеттере добавьте проверку условия, что сторона должна быть неотрицательной.

class Square:
    def __init__(self, side=0) -> None:
        if side > 0:
            self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if side > 0:
            self.__side = side

    @property
    def area(self):
        return self.__side * self.__side


if __name__ == "__main__":
    sq_1 = Square(10)
    print(sq_1.side, sq_1.area)
    sq_1.side = 20
    print(sq_1.side, sq_1.area)
