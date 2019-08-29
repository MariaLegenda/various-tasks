
# АЛГОРИТМ СОРТИРОВКИ ВСТАВКАМИ
# Сложность: O(n^2) / если массив уже отсортирован O(n)
# Не требует доп памяти, устойчивая

# Принцип: 1. Из массива последовательно берется каждый элемент, кроме первого (i == 0)
         # 2. И вставляется в отсортированную часть массива


import random

size = int(input('Введите размер массива: '))
array = [i for i in range(size)]

random.shuffle(array) #перемешать элементы в массиве
print('Исходный массив:', array)


def insertion_sort(array):

    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
    return array


insertion_sort(array)
print(f'Отсортированный массив: {array}')






