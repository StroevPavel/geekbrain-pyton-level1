# coding: utf-8

import random
import math

# Уже изобретал эту функцию ранее для задания на курсе "Python. Быстрый старт"
def is_int(n):
    return int(n) == float(n)

num_list = []
sqr_list = []

# Добавил модуль random чтобы не задавать произвольный список чисел руками
for i in range(0,int(input("Задайте количество чисел в исходном массиве: "))):
	num_list.append(random.randrange(-100,100))

print('Исходный массив: ' + str(num_list))
print(' ')

i = 0
while i < len(num_list):
	if (num_list[i] >= 0):
		res = math.sqrt(num_list[i])
		if is_int(res):
			sqr_list.append(res)
			print('Число: ' + str(num_list[i]) + ' Ok!')
		else:
			print('Число: ' + str(num_list[i]) + ' | Извлеченный корень не целое число! (' + str(res) + ')')
	else: 
		print('Число: ' + str(num_list[i]) + ' | Корень невозможно извлечь!')
	i += 1

print(' ')
if len(sqr_list) > 0:
	print('Итоговый массив: ' + str(sqr_list))
else:
	print('Итоговый массив: пустой!')