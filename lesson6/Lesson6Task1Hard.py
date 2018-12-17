# coding: utf-8

"""
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
"""

import datetime

class Staff:
	# наш типовой работник
	def __init__(self, name, surname, rate, job, wrk_hours):
		self.name = name
		self.surname = surname
		self.rate = int(rate)
		self.job = job
		self.wrk_hours = int(wrk_hours)
		self.real_wrk_hours = 0
		self.salary = 0
		self.salary_bonus = 0
		self.count_date = ""

	# метод пытается получить данные о фактически отработанных часах работника
	def get_real_work_hours(self):
		with open('hours_of.txt', 'r', encoding='UTF-8') as f_hours:
			for i in f_hours.readlines():
				if i.split()[0] == self.name and i.split()[1] == self.surname:
					self.real_wrk_hours = int(i.split()[2])
					break
		f_hours.close()

	# метод расчета фактического размера з/п работника
	def get_salary(self):
		hour_rate = self.rate // self.wrk_hours
		# salary = 0
		if self.real_wrk_hours > self.wrk_hours: # переработка
			self.salary_bonus = (self.real_wrk_hours - self.wrk_hours) * hour_rate
			self.salary = self.real_wrk_hours * hour_rate + self.salary_bonus
		elif self.real_wrk_hours < self.wrk_hours: # недоработка
			self.salary = self.real_wrk_hours * hour_rate
		else: # все ровно
			self.salary = self.rate

		self.count_date = datetime.datetime.now()

	# метод вывода данных на экран по работнику
	def print_data(self):
		print("")
		print("Имя: " + self.name)
		print("Фамилия: " + self.surname)
		print("Должность: " + self.job)
		print("Ставка з/п (руб): " + str(self.rate))
		print("Норма часов (ч): " + str(self.wrk_hours))
		print("Фактически отработано часов (ч): " + str(self.real_wrk_hours))
		print("Начисленная з/п (руб): " + str(self.salary) + " (в том числе бонус за переработанные часы: " + str(self.salary_bonus) + ")")

	# метод вывода данных в файл *.csv по работнику
	def save_csv(self):
		with open('salary.csv', 'a', encoding='UTF-8') as f_salary:
			f_salary.write(self.count_date.strftime("%d-%m-%Y") + ';' + self.name + ';' + self.surname + ';' + str(self.rate) + ';' + self.job + ';' + str(self.wrk_hours) + ';' + str(self.real_wrk_hours) + ';' + str(self.salary))
			f_salary.write('\n')
		f_salary.close()
		print("Добавлена запись в salary.csv")

# создаем экземпляр класа и выполняем действия по расчету фактической з/п для каждого работника
def get_worker(file):
	f_worker = open(file, 'r', encoding='UTF-8')
	for i in f_worker.readlines():
		if i.count('Имя') != 1:
			# обработка строки (начинаем со второй, в первой шапка таблицы)
			name, surname, rate, job, wrk_hours = i.split()
			worker = Staff(name, surname, rate, job, wrk_hours) # создаем экземпляр класса 
			worker.get_real_work_hours() # пробуем получить данные о факт. отработанном времени
			worker.get_salary() # рассчитаем фактическую з/п
			worker.print_data() # распечатаем данные работника на экране
			worker.save_csv() # сохраним строку в CSV файл
	f_worker.close()

print("Привет! Для расчета заработной платы работников введите любой символ, результат работы будет сохранен в файле salary.csv")
print("Внимание! Для корректной работы убедитесь, что в папке с программой подготовлены файлы workers.txt и hours_of.txt!")
prs = input("Для выходы нажмите [0] ")
if prs != "0":
	get_worker('workers.txt')
	print("")
	print("Работа завершена, откройте salary.csv, внимание, кодировка UTF-8!")
	print("Спасибо!")
else:
	print("Пока!")