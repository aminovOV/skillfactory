import os

# start_path = os.getcwd()  # save current path to variable
# print(start_path)  # print saved path
# os.chdir("..")  # go to folder in the upper level
# print(os.getcwd())  # print current path
# os.chdir(start_path)  # go to saved path
# print(os.getcwd())  # print current path
# print(os.listdir())  # print content of the current folder
# if 'func.py' in os.listdir(r"C:\Users\oleg\Documents\GitHub\skillfactory\C3"):
#     print('file in the folder')
# print(os.path.join(start_path, 'func.py'))
# print(os.path.join(r"C:\Users\oleg\Documents\GitHub\skillfactory\C3", 'func.py'))


# def walk_desc(path=None):
#     start_path = path if path is not None else os.getcwd()
#
#     for root, dirs, files in os.walk(start_path):
#         print("Текущая директория", root)
#         print("---")
#
#         if dirs:
#             print("Список папок", dirs)
#         else:
#             print("Папок нет")
#         print("---")
#
#         if files:
#             print("Список файлов", files)
#         else:
#             print("Файлов нет")
#         print("---")
#
#         if files and dirs:
#             print("Все пути:")
#         for f in files:
#             print("Файл ", os.path.join(root, f))
#         for d in dirs:
#             print("Папка ", os.path.join(root, d))
#         print("===")
#
#
# walk_desc()

# f = open('path/to/file', 'filemode', encoding='utf8')
# r — открыть на чтение (по умолчанию);
# w — перезаписать и открыть на запись (если файла нет, то он создастся);
# x — создать и открыть на запись (если уже есть — исключение);
# a — открыть на дозапись (указатель будет поставлен в конец);
# t — открыть в текстовом виде (по умолчанию);
# b — открыть в бинарном виде.

# f = open('test1.txt', 'w', encoding='utf8')
# f.write('Hello\nHow are you?\n')
# f.write('How are you?\n')
# f.close()

# f = open('test1.txt', 'r', encoding='utf8')
# print(f.read(2))
# print(f.read())
# f.close()

# writelines — записывает список строк в файл;
# readline — считывает из файла одну строку и возвращает её;
# readlines — считывает из файла все строки в список и возвращает их.

# f = open('test1.txt', 'a', encoding='utf8')
# sequence = ["I'm fine\n", "And you?\n"]
# f.writelines(sequence)
# f.close()

# f = open('test1.txt', 'r', encoding='utf8')
# print(f.readlines())
# f.close()

# f = open('test1.txt', 'r', encoding='utf8')
# print(f.readline())
# print(f.readline())
# print(f.read(6))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test1.txt')
# for line in f:
#     print(line, end='')
# f.close()

# with open('test1.txt', 'r', encoding='utf8') as f:
#     for line in f:
#         print(line, end='')

# with open('input.txt', 'w', encoding='utf8') as f:
#     f.write('1-st string\n')
#     f.write('2-nd string\n')
#     f.write('3-rd string\n')
#     f.close()
#     with open('output.txt', 'w', encoding='utf8') as output:
#         with open('input.txt', 'r', encoding='utf8') as input:
#             for line in input:
#                 output.write(line)

# with open('numbers.txt', 'w', encoding='utf8')as f:
#     f.write('10\n')
#     f.write('22\n')
#     f.write('35\n')
#     f.write('1\n')

# with open('numbers.txt', 'r', encoding='utf8') as f:
#     min_ = max_ = int(f.readline())  # считали первое число
#     for line in f:
#         num = int(line)
#         if num > max_:
#             max_ = num
#         if num < min_:
#             min_ = num
#     with open('result.txt', 'w', encoding='utf8') as f:
#         f.write(f'the sum of the minimal and maximal numbers in the file "numbers.txt" == {min_ + max_}')

# with open('numbers.txt', 'r', encoding='utf8') as f:
#     a = f.readlines()
#     print(int(max(a)) + int(min(a)))
#     with open('result.txt', 'w', encoding='utf8') as r:
#         r.write(f'the sum of the minimal and maximal numbers in the
#         file "numbers.txt" == {int(max(a)) + int(min(a))}')

# with open('stud.txt', 'r', encoding='utf8') as f:
#     a = f.readlines()
#     for line in a:
#         if '1' in line:
#             print(line)
#         if '2' in line:
#             print(line)

# with open('stud.txt', 'r', encoding='utf8') as f:
#     a = f.readlines()
#     for line in a:
#         if int(line.split()[-1]) < 3:
#             print(line.split()[:-1])

# with open('stud.txt', encoding="utf8") as file:
#     for line in file:
#         points = int(line.split()[-1])
#         if points < 3:
#             name = " ".join(line.split()[:-1])
#             print(name)


# with open('stud1.txt', 'w', encoding="utf8") as file:
#     with open('stud.txt', 'r', encoding="utf8") as f:
#         for line in f:
#             line = line[::-1]
#             file.write(line)

# with open('input.txt', 'r') as input_file:
#    with open('stud2.txt', 'w') as output_file:
#        for line in reversed(input_file.readlines()):
#            output_file.write(line)

from datetime import datetime
import time  # проверять действие измерителя будем с помощью библиотеки time


# вся суть этого измерителя заключается в том, что мы считаем разницу в секундах между открытием и
# закрытием контекстного менеджера
# class Timer:
#     def __init__(self):
#         pass
#
#     def __enter__(self):  # Этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект,
#         # чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто
#         # верните этот объект через return
#         self.start = datetime.utcnow()
#         return None
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
#         print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")
#
#
# with Timer():
#     time.sleep(2)  # засыпаем на 2 секунды

# from datetime import datetime
# import time
#
# from contextlib import contextmanager  # импортируем нужный нам декоратор


# @contextmanager  # оборачиваем функцию в декоратор contextmanager
# def timer():
#     start = datetime.utcnow()
#     yield  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
#     print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")
#
#
# with timer():
#     time.sleep(2)

# Задание 3.5.6
# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
# В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к файлу,
# который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
# При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
# При выходе из контекстного менеджера файл должен закрываться.
# (Эталоном работы можно считать контекстный менеджер open).

class File:
    def __init__(self, path, type_):
        self.file = open(path, type_, encoding="utf8")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File("stud.txt", 'r') as f:
    print(f.read())
