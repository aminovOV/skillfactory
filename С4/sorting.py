from time import time as t
import random  # модуль, с помощью которого перемешиваем массив

"""
# Naive sort

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7] 

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок
s_1 = t()
while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счетчику
    
    random.shuffle(array)  # перемешиваем массив
    
    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_sort = False
            break
            
#print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(count)
# 290698
#print(t() - s_1)
"""

# Selection sort

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# array = list(range(100))
# random.shuffle(array)
# print(array)
s = t()
count = 0
count_1 = 0
for i in range(len(array)): # проходим по всему массиву

        idx_min = i # сохраняем индекс предположительно минимального элемента
        for j in range(i+1, len(array)):
                count_1 += 1
                if array[j] < array[idx_min]:
                        idx_min = j

        if i != idx_min: # если индекс не совпадает с минимальным, меняем
                array[i], array[idx_min] = array[idx_min], array[i]
                count += 1

print(array, t() - s, count, count_1)
