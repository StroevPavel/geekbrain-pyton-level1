# coding: utf-8

"""
Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
"""

def fibonacci(n, m):
	i = 2 
	while i < m:
		#fibn = fib_row[i - 1] + fib_row[i - 2]
		#fib_row.append(fibn)
		fib_row.append(fib_row[i - 1] + fib_row[i - 2])
		i += 1
	return fib_row[n - 1:m]

fib_row = [0, 1]

print("Задайте диапазон номеров чисел ряда фибоначи (например: с 5 по 12)")
f1 = int(input("Стартуем с: "))
f2 = int(input("считаем до: "))

print(fibonacci(f1, f2))

input("Нажмите Enter чтобы закончить...")