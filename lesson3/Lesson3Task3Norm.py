# coding: utf-8

"""
Напишите собственную реализацию стандартной функции filter
"""

import random

# будем реализовывать фильтр на примере filter(lambda x: x > 50, count))

def make_filter(in_count,in_fun):
	res = []
	i = 0
	while i < len(in_count):
		if in_fun(in_count[i]) == True:
			res.append(in_count[i])
		i += 1
	return res

count = []
filtred_by_filter = []

i = 0
while i < 20:
	count.append(random.randrange(0,100))
	i += 1

print("Исходный массив: " + str(count))

filtred_by_filter = list(filter(lambda x: x > 50, count))
print("Результат сортировки штатным filter(): " + str(filtred_by_filter))
print("Результат сортировки (свой аналог): " + str(make_filter(count,(lambda x: x > 50))))