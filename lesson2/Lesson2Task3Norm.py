# coding: utf-8

import random

num_list = []

for i in range(0,int(input("Задайте количество чисел в массиве: "))):
	num_list.append(random.randrange(-100,100))

print("Итог:")
print(num_list)