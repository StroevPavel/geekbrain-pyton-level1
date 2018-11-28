# coding: utf-8

import math

print("Привет! Давай решим уравнение ax² + bx + c = 0")
print("Введи значения коэффициентов a, b и c твоего уровнения (это целые числа)")
a = int(input("Коэффициент 'a': "))
b = int(input("Коэффициент 'b': "))
c = int(input("Коэффициент 'c': "))

diskriminant = b*b - 4*a*c

if diskriminant > 0:
	x1 = (-1*b + math.sqrt(diskriminant)) / 2*a
	x2 = (-1*b - math.sqrt(diskriminant)) / 2*a
	print("Ответ (D>0, 2 корня): X1=" + str(x1) + " и X2=" + str(x2))
elif diskriminant == 0:
	x1 = (-1*b) / (2*a)
	print("Ответ (D<0, 1 корень): X=" + str(x1))
else:
	print("Ответ: уравнение не имеет корней, так как D<0 (D=" + str(diskriminant) + ")")