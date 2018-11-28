# coding: utf-8

res = 0
num = int(input("Введите целое число: "))
while num >= 10:
	figure = num % 10
	num = num // 10
	if figure > res:
		res = figure
if num > res:
	res = num

print("Самая большая цифра в числе - " + str(res))