# coding: utf-8

import os

def check_is_dir(dir_path):
	if os.path.exists(dir_path):
		if os.path.isdir(dir_path):
			return True
		else: 
			print("Указан неверный путь, это не папка, попробуйте снова...")
			return False
	else:
		print("Указан неверный путь, попробуйте снова...")
		return False

def change_dir(dir_path):
	if check_is_dir(dir_path):
		try:
			os.chdir(dir_path) 
			print('Задача выполена! Текущая папка: ' + os.getcwd())
		except:
			print('Что-то пошло не так! Попробуйте снова...')

def get_dir_list(dir_path):
	if check_is_dir(dir_path):
		print('Текущая папка: ' + os.getcwd())
		print('Содержимое папки: ')
		print(os.listdir(dir_path))

def del_dir_list(dir_path):
	if check_is_dir(dir_path):
		try:
			os.rmdir(dir_path) 
			print('Задача выполена! Удалена папка: ' + dir_path)
		except:
			print('Что-то пошло не так! Возможно папка не пустая, или у вас нет прав для ее удаления! Попробуйте снова...')

def make_dir(dir_path):
	try:
		os.mkdir(dir_path)
		print('Задача выполена! Создана папка: ' + dir_path)
	except FileExistsError:
		print('Такая директория уже существует!')