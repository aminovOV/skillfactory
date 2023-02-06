# try:
#     raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
# except ArithmeticError:  # ловим его родителя
#     print("Hello from arithmetic error")

# try:
#     raise ZeroDivisionError
# except ZeroDivisionError:  # сначала пытаемся поймать наследника
#     print("Zero division error")
# except ArithmeticError:  # потом ловим родителя
#     print("Arithmetic error")

# class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
#     pass
#
#
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     pass
#
#
# try:
#     raise ChildException("message")  # поднимаем исключение-наследник
# except ParentException as e:  # ловим его родителя
#     print(e)  # выводим информацию об исключении

# class ParentException(Exception):
#     def __init__(self, message,
#                  error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
#         super().__init__(message)  # помним про вызов конструктора родительского класса
#         print(f"Errors: {error}")  # печатаем ошибку
#
#
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     def __init__(self, message, error):
#         super().__init__(message, error)
#
#
# try:
#     raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
# except ParentException as e:
#     print(e)  # выводим информацию об исключении

# while True:
#     x = input('Input the number: ')
#     try:
#         if x == '10':
#             raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
#     except ZeroDivisionError:  # ловим его родителя
#         print("Not OK. Input the number: ")
#     else:
#         print('OK')
#         break

# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.


# class NonPositiveDigitException(ValueError):
#     pass


# class Square:
#     def __init__(self, side=None):
#         self.__side = side
#
#     def area(self, side):
#         self.__side = side
#         try:
#             if self.__side <= 0:
#                 raise NonPositiveDigitException('square side < 0 or = 0')
#         except ValueError as e:
#             print(e)
#         else:
#             print(f'{self.__side * self.__side} m2')
#
#
# sq_1 = Square()
# sq_1.area(-5)

class NonPositiveDigitException(ValueError):
    pass


class Square:
    def __init__(self, a):
        if a <= 0:
            raise NonPositiveDigitException('Неправильно указана сторона квадрата')


sq = Square(-5)
