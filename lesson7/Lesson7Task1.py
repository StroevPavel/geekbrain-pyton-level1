# coding: utf-8

"""
== Лото ==
"""

import random

# класс нашей игровой карты (15 случайных цифр из диапазона 1-90, формат карты 3 строки по 9 ячеек и по 5 чисел в строке)
class GameCard:
	def __init__(self, gamer):
		self.gamer = gamer
		self.card_fig = []
		self.burrel = 0

	# создаем новую карту для игры
	def gen_new_card(self):

		# сортировка пузырьки, хотел проверить работу функции внутри метода класса )
		def sort_to_max(origin_list):
			counter = 1 # длина списка - 1
			while counter < len(origin_list):
				for i in range(len(origin_list) - counter):
						if origin_list[i] > origin_list[i+1]:
							origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
				counter += 1
			return(origin_list)

		# получаем 15 случайных чисел (диапазон от 1 до 90)
		raw_card = []
		i = 0
		fig = 0
		while i < 15:
			# проверяем на дубликаты, числа уникальные
			fig = random.randrange(1,90)
			if raw_card.count(fig) == 0:
				raw_card.append(fig)
				i += 1
		i = 0
		while i < 3:
			if i == 0: 
				self.card_fig.append(sort_to_max(raw_card[:5]))
			if i == 1: 
				self.card_fig.append(sort_to_max(raw_card[5:10]))
			if i == 2: 
				self.card_fig.append(sort_to_max(raw_card[10:]))
			i += 1
		# распределяем случайным образом в каждой строке по 4 "пробела" чтобы имитировать строку карты в 9 ячеек.
		i = 0
		while i < 3:
			j = 0
			while j < 4:
				fig = random.randrange(0,len(self.card_fig[i]))
				if fig == len(self.card_fig[i]): 
					self.card_fig[i].append(" ")
				else: 
					self.card_fig[i].insert(fig, " ")
				j += 1
			i += 1

	# проверяем есть ли выпавшее число на карте
	def check_burrel(self):
		if self.card_fig[0].count(self.burrel) > 0:
			return True
		elif self.card_fig[1].count(self.burrel) > 0:
			return True
		elif self.card_fig[2].count(self.burrel) > 0:
			return True
		else: 
			return False

	# вычеркиваем выпавшее на боченке число из карточки
	def off_burrel(self):
		if self.card_fig[0].count(self.burrel) > 0:
			self.card_fig[0][self.card_fig[0].index(self.burrel)] = "-"
		elif self.card_fig[1].count(self.burrel) > 0:
			self.card_fig[1][self.card_fig[1].index(self.burrel)] = "-"
		elif self.card_fig[2].count(self.burrel) > 0:
			self.card_fig[2][self.card_fig[2].index(self.burrel)] = "-"

	# проверяем, все ли числа вычеркнуты, или еще нет
	def check_win(self):
		if (self.card_fig[0].count("-") + self.card_fig[1].count("-") + self.card_fig[2].count("-")) == 15:
			return True
		else:
			return False
	
	# выводим карту игрока на экран
	def print_card(self):
		# print(self.card_fig)
		for i in self.card_fig: 
			print(i)

# главное меню
def show_main_menu():
	print("")
	print("[1] Начать новую игру")
	print("[0] Выйти из приложения")

# игровое меню
def show_game_menu():
	print("")
	print("[1] Вытаскиваем следующий бочонок...")
	print("[2] Показать карты игроков")
	print("[3] Показать статистику")
	print("[0] Прервать игру и выйти из приложения")

# главное меню
def show_barrel_menu():
	print("")
	print("[1] Зачеркнуть цифру (если цифра есть на Вашей карточке)")
	print("[2] Продолжить (если цифры на Вашей карточке нет)")

# начинаем новую игру
def start_new_game(name, gamer1, gamer2):
	# создаем новые игровые карточки
	gamer1.gen_new_card()
	gamer2.gen_new_card()
	print("")
	print("Запуск новой игры...")
	show_gamer_cards(name, gamer1, gamer2)

# Показать карты игроков
def show_gamer_cards(name, gamer1, gamer2):
	print("")
	print("Карта игрока PC:")
	gamer1.print_card()
	print("")
	print("Карта игрока " + name + ":")
	gamer2.print_card()

# Показать статистику
def show_stats(name, done_burrels):
	print("")
	print("Уже вытащили бочонки с номерами:")
	print(done_burrels)

# Вытаскиваем следующий бочонок
def take_burrel(name, gamer1, gamer2, done_burrels):
	i = 0
	# получаем случайный номер 1-90, но не из тех, которые уже вытаскивали ранее
	while i == 0:
		fig = random.randrange(1,90)
		if done_burrels.count(fig) == 0:
			done_burrels.append(fig)
			i += 1
	gamer1.burrel = fig
	gamer2.burrel = fig
	print("")
	print("Вытащили бочонок номер")
	print("--== " + str(fig) + " ==--")
	# проверяем карточки
	show_barrel_menu()
	answer = 10

	while answer > 2:
		answer = int(input("Какое действие выполнить? (введите номер) "))
		if answer == 1: # Зачеркнуть цифру (если цифра есть на Вашей карточке)
			if gamer2.check_burrel(): # да, цифра есть
				gamer2.off_burrel()
				if gamer1.check_burrel():
					gamer1.off_burrel()
				return 3
			else: # нет, цифры нет
				return 1
		elif answer == 2: # Продолжить (если цифры на Вашей карточке нет)
			if gamer2.check_burrel(): # да, цифра есть 
				return 2
			else: # нет, цифры нет
				if gamer1.check_burrel():
					gamer1.off_burrel()
				return 3
		else:
			print("Неверная команда, попробуйте снова...")

def game_over(res):
	print("")
	if res == 1:
		print("На Вашей карточке нет такой цифры!")
	elif res == 2:
		print("На Вашей карточке есть такая цифра!")
	print("Увы, это проигрыш...")

def main():
	print("Python startup...ЛОТО!")
	print("Привет! Начинаем игру ...")

	answer = 10
	name = ""
	done_burrels = []

	while answer != 0:
		show_main_menu()
		answer = int(input("Какое действие выполнить? (введите номер) "))
		if answer == 1: # Начать новую игру
			name = input("Как Ваше имя? ")
			# создаем экземпляры классов для 2-х игроков
			gamer_pc = GameCard("PC")
			gamer_man = GameCard(name)
			# начинаем игру
			start_new_game(name, gamer_pc, gamer_man)
			while answer != 0:
				show_game_menu()
				answer = int(input("Какое действие выполнить? (введите номер) "))
				if answer == 1: # Следующий бочонок
					show_gamer_cards(name, gamer_pc, gamer_man)
					res = take_burrel(name, gamer_pc, gamer_man, done_burrels)
					if res < 3: # неверно выбрано действие и по условиям игры это проигрыш
						game_over(res)
						answer = 0
					else: # все ок
						show_gamer_cards(name, gamer_pc, gamer_man)
						# проверяем, вдруг кто-то из игроков вычеркнул все цифры и выиграл
						if (gamer_pc.check_win()) and (gamer_man.check_win()):
							print("")
							print("Ничья!!!")
							answer = 0
						elif (gamer_pc.check_win()):
							print("")
							print("Победил игрок: " + gamer_pc.name)
							answer = 0
						elif (gamer_man.check_win()):
							print("")
							print("Победил игрок: " + gamer_man.name)
							answer = 0
				if answer == 2: # Показать карты игроков
					show_gamer_cards(name, gamer_pc, gamer_man)
				if answer == 3: # Показать статистику
					show_stats(name, done_burrels)
				if answer == 0: # Прервать игру и выйти из приложения
					pass
				else:
					# print("Неверная команда, попробуйте снова...")
					pass
		elif answer == 0: # Выйти из приложения
			pass
		else:
			# print("Неверная команда, попробуйте снова...")
			pass

	print("")
	print("Пока!")

# Запускаем Лото!
if __name__ == "__main__":
	main()