import time
# import sys
# sys.setrecursionlimit(100050)
# books = ['z', 'y', 'w', 's', 'a']
# # # print(books.sort())
# # b = []
# book1 = books[0][0]
# for i, value in enumerate(books):
#     if value[0] < book1:

# print(b)
# matrix = [['*']*6 for _ in range(6)]
#
# for row in matrix:
#     for element in row:
#         print(f'| {element}', end=" ")
#     print('|')


# def p(n):
#     while n != 0:
#         print(n)
#         return p(n-1)
#
#
# def x(n):
#     if n == 0:
#         return
#     else:
#         x(n-1)
#         print(n)


# def z(n):
#     while True:
#         n -= 1
#         print(n)
#         if n == 0:
#             break
#
#
# def y(n):
#     for i in range(n-1):
#         n -= 1
#         print(n)
#         if n == 0:
#             break


# start = time.time()
# p(100000)
# print("--- %s seconds ---" % (time.time() - start))

# start_ = time.time()
# x(100000)
# print("--- %s seconds ---" % (time.time() - start_))

# start__ = time.time()
# z(100000)
# print("--- %s seconds ---" % (time.time() - start__))

# start___ = time.time()
# y(100000)
# print("--- %s seconds ---" % (time.time() - start___))

def par_checker(string):
    stack = []  # инициализируем стек
    dict_ = {')': '(', ']': '[', '}': '{'}

    for s in string:  # читаем строку посимвольно
        if s in dict_.values():  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s in dict_.keys():
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] in dict_.values():
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                print('error')
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


par_checker('(5+6)*(7+8)/(4+3))')
dict_ = {')': '(', ']': '[', '}': '{'}
print(dict_.values())
print(dict_.keys())
print('(' in dict_.values())
print(dict_.keys())
print(')' in dict_.keys())
