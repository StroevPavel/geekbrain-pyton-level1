# coding: utf-8

"""
Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
произвольными целыми цифрами, в результате в файле должно быть
2500-значное произвольное число.
Найдите и выведите самую длинную последовательность одинаковых цифр
в вышезаполненном файле.
"""

import random

# генератор числа + собираем в строку
txt = []
i = 0
while i < 2500:
	if i == 0:
		txt.append(str(random.randrange(1,9)))
	else :
		txt.append(str(random.randrange(0,9)))
	i += 1
txt_to_file = ''.join(txt).split(' ')

# пишем файл + читаем из файла
with open('task3.txt', 'w', encoding='UTF-8') as file:
	file.write(str(txt_to_file))

with open('task3.txt', 'r', encoding='UTF-8') as file:
	txt_from_file = list(file.read())

# ищем самую длинную последовательность одинаковых цифр
# возможно в той части вкралась ошибка, не успеваю проверить результат, логика кажется верной
i = 0
j = 0
f = 0
max_len = 0
fig = 0
while i < len(txt_from_file):
	if len(txt_from_file) > (i+1):
		if txt_from_file[i] == txt_from_file[i+1]:
			j += 1
			f = txt_from_file[i]
			print(txt_from_file[i] + txt_from_file[i+1] + str(f) + str(j))
		else:
			if j > max_len:
				max_len = j
				fig = f
				j = 0
				f = 0
	else:
		if j > max_len:
			max_len = j
			fig = f
	i += 1

print("Число (записано в файл task3.txt в папке с кодом программы): ")
print(txt_to_file)

print("Самая длинная последовательность одинаковых цифр:")
print("Цифра: " + str(fig) + "; длина последовательности: " + str(max_len + 1))