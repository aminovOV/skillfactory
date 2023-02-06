# Создадим класс Queue - нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    def get_(self):
        return self.tasks

    def is_empty(self):
        return all(_ == 0 for _ in self.tasks)

    def size(self):
        size_ = 0
        for _ in self.tasks:
            if _ > 0:
                size_ += 1
        return size_

    def add(self):
        if self.tasks[-1] == self.max_size:
            return False
        else:
            self.task_num += 1
            self.head += 1
            self.tasks.append(self.task_num)
            self.tasks.pop(0)
            print(f'Задача №{self.task_num} добавлена')
            return True

    def show(self):
        print(f"Задача №{self.head} в приоритете")
        return

    def do(self):
        num = int(input('Введите номер задачи: '))
        self.tasks.pop(self.tasks.index(num))
        print(f"Задача №{num} выполнена")
        return True

    def exit(self):
        print(self.tasks)
        exit()


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break

    if cmd == 'get_':
        print(q.get_())
    # else:
    #     print("Введена неверная команда")
