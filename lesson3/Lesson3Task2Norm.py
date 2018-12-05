# coding: utf-8

"""
Напишите функцию, сортирующую принимаемый список по возрастанию.
Для сортировки используйте любой алгоритм (например пузырьковый).
Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
"""

# пузырьковый
def sort_to_max(origin_list):
	counter = 1 # длина списка - 1
	while counter < len(origin_list):
		for i in range(len(origin_list) - counter):
				if origin_list[i] > origin_list[i+1]:
					origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
		counter += 1
	return(origin_list)
	
list1 = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("Сортировка по возрастанию, исходный: " + str(list1))
print("Сортированный: " + str(sort_to_max(list1)))