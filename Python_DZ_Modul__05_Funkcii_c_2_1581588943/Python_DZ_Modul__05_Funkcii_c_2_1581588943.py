print("Добрый день. Это домашняя работа по курсу Python,\nвыполненная студентом группы Python23 академии ТОР, Челябинск\n"
	  "Щур Александром Николаевичем.\nПреподаватель Андрей Комаров\n"
	  "________________________________________________________________________________________________________________")

'''
Задание 1
Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве па-
раметра. Полученный результат возвращается из функции.
'''
'''
def multipl_list(a):
	n = 1
	for el in a:
		n *= el
	return print(n)

multipl_list([1, 2, 3, 4, 5])
'''
'''
Задание 2
Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.
'''
'''
def list_min(a):
	return print(min(a))

list_min([1,6,7,4,8])
'''
'''
Задание 3
Напишите функцию, определяющую количество про-
стых чисел в списке целых. Список передаётся в качестве
параметра. Полученный результат возвращается из функции.
'''
'''
def list_simple(a):
	count = 0
	for x in a:
		if x == 1 or x == 2 or x == 3 or x == 5 or x == 7:
			count += 1
		elif x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x != 0:
			count += 1
		else:
			pass

	return print(count)

list_simple([-10,25,0,7, 190,77, 31])
'''
'''
Задание 4
Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов.
'''
'''
def delete_list(a, b):
	count = 0
	for x in a:
		if x == b:
			a.remove(x)
			count += 1
	return print(count)

delete_list ([1, 3, 4, 5, 6, 5, 4, 5,3,6,5], 5)
'''

'''
Задание 5
Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков.
'''
'''
def add_lists(a, b):
	common_list = a + b

	return (print(common_list))

add_lists([1, 2, 3], ['a', 'b', 'c'])
'''

'''
Задание 6
Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержа-
щий полученные результаты.
'''
'''
def list_step(a, b):
	new_list = []
	for x in a:
		new_list.append(x ** b)
	return print(new_list)

list_step([1,2,3], 2)
'''
print("________________________________________________________________________________________________________________\n"
	  "Благодарю вас за пользование моей программой.\n"
      "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
      "Спасибо за внимание.")