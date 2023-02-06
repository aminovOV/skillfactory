"""
def find(array, element):
    count = 0
    for i, a in enumerate(array):
        if a == element:
            count +=1 
            return i
    return count

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))
"""
"""
def count(arr, el):
    count = 0
    for i, a in enumerate(arr):
        if a == el:
            count +=1 
    return count

arr = list(map(int, input().split()))
el = int(input())

print(count(arr, el))
"""
def binary_search(array, element, left, right): 
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    
    middle = (right+left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else:  # иначе в правой
        return binary_search(array, element, middle+1, right)


element = int(input())
array = [i for i in range(1,100)] # 1,2,3,4,...
# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 98))