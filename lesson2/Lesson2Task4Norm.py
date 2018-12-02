# coding: utf-8

import random

num_list = []
num_list1 = []
num_list2 = []

for i in range(0,int(input("Задайте количество чисел в исходном массиве (число больше 1): "))):
	num_list.append(random.randrange(1,10))
print('Исходный массив: ' + str(num_list))

num_list1 = list(set(num_list))
print('Неповторяющиеся элементы исходного массива (всего ' + str(len(num_list1)) + ' значений): ' + str(num_list1))

i = 0
while i < len(num_list):
	j = 0
	dbl = 0
	while j < len(num_list):
		if (num_list[i] == num_list[j]) & (i != j):
			dbl = 1
			break
		j += 1

	if dbl == 0:
		num_list2.append(num_list[i])

	dbl = 0
	i += 1
print('Элементы исходного массива, которые не имеют повторений (всего ' + str(len(num_list2)) + ' значений): ' + str(num_list2))