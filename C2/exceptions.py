# # # # try:  # Добавляем конструкцию try-except для отлова нашей ошибки
# # # #     print("Перед исключением")
# # # #     # теперь пользователь сам вводит числа для деления
# # # #     a = int(input("a: "))
# # # #     b = int(input("b: "))
# # # #     c = a / b  # здесь может возникнуть исключение деления на ноль
# # # #     print(c)  # печатаем c = a / b, если всё хорошо
# # # # except ZeroDivisionError as e:  # Добавляем тип именно той ошибки, которую хотим отловить.
# # # #     print(e)  # Выводим информацию об ошибке
# # # #     print("После исключения")
# # # #
# # # # print("После исключения")
# # #
# # # try:
# # #     print("Перед исключением")
# # #     a = int(input("a: "))
# # #     b = int(input("b: "))
# # #     c = a / b
# # #     print(c)  # печатаем c = a / b, если всё хорошо
# # # except ZeroDivisionError as e:
# # #     print("После исключения")
# # # else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно
# # # (т.е. не вылетело никакого исключения).
# # #     print("Всё отлично")
# # # finally:  # код в блоке finally выполнится в любом случае, при выходе из try-except
# # #     print("Finally на месте")
# # #
# # # print("После исключения")
# #
# # age = int(input("How old are you?"))
# #
# # if age > 100 or age <= 0:
# #     raise ValueError("Тебе не может быть столько лет")
# #
# # print(f"Тебе {age} лет!")  # Возраст выводится, только если пользователь ввёл правильный возраст.
#
# try:
#     age = int(input("How old are you?"))
#
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError:
#     print("Неправильный возраст")
#
# print(f"You are {age} years old!")  # Возраст выводится, только если пользователь ввёл правильный возраст.

# Создайте скрипт, который будет в input() принимать строки и их необходимо будет конвертировать в числа.
# Добавьте try-except на то, чтобы строки могли быть конвертированы в числа. В случае удачного выполнения
# скрипта должно быть выведено сообщение: «Вы ввели правильное число».
# В конце скрипта обязательно напишите: «Выход из программы».
# Примечание: для отлова ошибок используйте try-except, а также блоки finally и else.
# Примеры входов и выходов:
#
# Введите число: 1
# Вы ввели 1
# Мы на выходе
# введите число: -3
# Вы ввели -3
# Мы на выходе.
# Введите число: razdvatri
# Вы ввели неправильное число
# Мы на выходе

try:
    x = int(input(": "))
except ValueError:
    print('Вы ввели не число')
else:
    print('Вы ввели правильное число')
finally:
    print('Выход из программы')