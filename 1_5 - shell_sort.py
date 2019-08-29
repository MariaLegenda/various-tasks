
# АЛГОРИТМ СОРТИРОВКИ ШЕЛЛА
# Сложность: O(n^2) / O(n (log n)^2) или O(n^(3/2)
# Не требует доп памяти, неустойчивая

# Принцип: 1. Выбираем шаг для сравнения элементов
         # 2. Сравниваем последовательно элементы массива,
         #    находящиеся один от другого на расстоянии шага
         # 3. Уменьшаем шаг и повторяем п.1, 2

import random

size = int(input('Введите размер массива: '))
array = [i for i in range(size)]

random.shuffle(array) #перемешать элементы в массиве
print('Исходный массив:', array)

def shell_sort(array):
    
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'
    
    #свой генератор
    def new_increment(array):
        
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750] # шаги

        # проверим длину массива и исключим шаги, которые нам не подходят
            while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()


    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]

shell_sort(array)
print(f'Отсортированный массив: {array}')




