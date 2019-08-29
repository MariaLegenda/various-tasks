
# АЛГОРИТМ СОРТИРОВКИ ВЫБОРОМ
# Сложность: O(n^2) 
# Не требует доп памяти, устойчивая/неустойчивая

# Принцип: 1. Найти наименьший элемент в неотсортированной части массива
         # 2. Поменять его местами с первым элементов в неотсортированной части массива
         # 3. Повторять п.1, 2 пока массив не будет отсортирован


import random

size = int(input('Введите размер массива: '))
array = [i for i in range(size)]

random.shuffle(array) # перемешать элементы в массиве
print(f'Исходный массив: {array}')


def selection_sort(array):

    for i in range(len(array)):
        idx_min = i
       
        for j in range(i+1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
               
        array[idx_min], array[i] = array[i], array[idx_min]
    
    return array


selection_sort(array)
print(f'Отсортированный массив: {array}')





