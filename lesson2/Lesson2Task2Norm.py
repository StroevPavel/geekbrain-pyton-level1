# coding: utf-8

import datetime

days = ['первое', 'второе', 'третье', 'четвёртое','пятое', 'шестое', 'седьмое', 'восьмое','девятое', 'десятое', 
'одиннадцатое', 'двенадцатое','тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое','двадцать первое', 'двадцать второе', 'двадцать третье',
'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое','двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
'тридцатое', 'тридцать первое']

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня','июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

d = datetime.date.today()

print('Текущая дата: ' + days[d.day - 1] + ' ' + months[d.month - 1]  + ' ' + str(d.year) + ' года')