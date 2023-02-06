# Первый должен содержать число Пи в виде константы 3.14 и две функции, которые будут считать
# площадь круга и прямоугольника.
# Второй модуль должен импортировать первый, далее запрашивать у пользователя размеры круга и квадрата.
# В результате выводить, какая из фигур больше.


PI = 3.14


def circle_area(radius):
    area = PI * float(radius)**2
    return area


def rectangle_area(side_1, side_2):
    area = float(side_1) * float(side_2)
    return area


if __name__ == "__main__":
    assert circle_area(5) == 78.5
    assert rectangle_area(5, 4) == 20
