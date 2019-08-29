# СОРТИРОВКА ПУЗЫРЬКОМ

import random

size = int(input('Введите размер массива: '))
array = [random.randint(-100,100) for i in range(size)]
print(f'Исходный массив: {array}')


def bubble_sort(array):

	way = True
	n = 1

	while n < len(array) and way:
		way = False
		for i in range(len(array) - n):
			if array[i] > array[i + 1]:
				way = True
				array[i], array[i + 1] = array[i + 1], array[i]
		n += 1

	return(array)
 

print(f'Отсортированный массив: {bubble_sort(array)}')





