print("Добрый день. Это домашняя работа по курсу Python,\nвыполненная студентом группы Python23 академии ТОР, Челябинск\n"
	  "Щур Александром Николаевичем.\nПреподаватель Андрей Комаров\n"
	  "________________________________________________________________________________________________________________")

'''
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеариф-
метическое каждой группы.
'''
'''
a = int(input("Введите первое число цифрой: "))
b = int(input("Введите второе число цифрой: "))

even_list = []
odd_list = []
list_9 = []
even_sum = 0
even_mean = 0
odd_sum = 0
odd_mean = 0
sum_9 = 0
mean_9 = 0

main_list = [i for i in range(a, b+1)]
print(main_list)

for i in range(0, len(main_list)):
	if main_list[i] % 2 == 0 and main_list[i] != 0:
		even_list.append(main_list[i])

	if main_list[i] % 2 != 0 and main_list[i] != 0:
		odd_list.append(main_list[i])

	if main_list[i] % 9 == 0 and main_list[i] != 0:
		list_9.append(main_list[i])


print(even_list)
print(odd_list)
print(list_9)

if len(list_9) == 0:
	even_sum = sum(even_list)
	odd_sum = sum(odd_list)
	odd_mean = odd_sum / len(odd_list)
	even_mean = even_sum / len(even_list)
	print(f"Сумма четных = {even_sum}\n"
		f"Сумма нечетных = {odd_sum}\n"
		f"Среднее четных = {even_mean}\n"
		f"Среднее нечетных = {odd_mean}\n"
		"Нет кратных 9 чисел")
elif len(even_list) == 0:
	odd_sum = sum(odd_list)
	sum_9 = sum(list_9)
	mean_9 = sum_9 / len(list_9)
	odd_mean = odd_sum / len(odd_list)
	print(f"Сумма нечетных = {odd_sum}\n"
		f"Сумма кратных 9 = {sum_9}\n"
		f"Среднее нечетных = {odd_mean}\n"
		f"Среднее кратных 9 = {mean_9}\n"
		"Нет четных чисел")
elif len(odd_list) == 0:
	even_sum = sum(even_list)
	sum_9 = sum(list_9)
	mean_9 = sum_9 / len(list_9)
	even_mean = even_sum / len(even_list)
	print(f"Сумма четных = {even_sum}\n"
		f"Сумма кратных 9 = {sum_9}\n"
		f"Среднее четных = {even_mean}\n"
		f"Среднее кратных 9 = {mean_9}\n"
		"Нет нечетных чисел")
else:
	even_sum = sum(even_list)
	odd_sum = sum(odd_list)
	sum_9 = sum(list_9)
	mean_9 = sum_9 / len(list_9)
	odd_mean = odd_sum / len(odd_list)
	even_mean = even_sum / len(even_list)
	print(f"Сумма четных = {even_sum}\n"
		f"Сумма нечетных = {odd_sum}\n"
		f"Сумма кратных 9 = {sum_9}\n"
		f"Среднее четных = {even_mean}\n"
		f"Среднее нечетных = {odd_mean}\n"
		f"Среднее кратных 9 = {mean_9}\n")
'''
'''
Задание 2
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране вертикальную линию из введенного символа,
указанной длины.
'''
'''
line_length = int(input("Введите длину строки цифрой: "))
line_symbol = input("Введите символ для заполнения строки: ")

line_list = [i for i in range(0, line_length)]

for i in range(0, line_length):
	print(f'{line_symbol}', sep='\n')
'''

'''
Задание 3
Пользователь вводит с клавиатуры числа. Если число
больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», если равно нулю
«Number is equal to zero». Когда пользователь вводит
число 7 программа прекращает свою работу и выводит
на экран надпись «Good bye!»
'''
'''
a = float(input("Введите число цифрой: "))

while a != 7:
	if a > 0:
		print('«Number is positive»')
		a = float(input("Введите число цифрой: "))
	elif a < 0:
		print('«Number is negative»')
		a = float(input("Введите число цифрой: "))
	elif a == 0:
		print('«Number is equal to zero»')
		a = float(input("Введите число цифрой: "))
else:
	print('«Good bye!»')
'''
'''
Задание 4
Пользователь вводит с клавиатуры числа. Програм-
ма должна подсчитывать сумму, максимум и минимум,
введенных чисел. Когда пользователь вводит число 7
программа прекращает свою работу и выводит на экран
надпись «Good bye!»
'''
'''
numbers_list = []
a = float(input("Введите число цифрой: "))

while a != 7:
		numbers_list.append(a)
		list_sum = sum(numbers_list)
		list_min = min(numbers_list)
		list_max = max(numbers_list)
		print(f'Сумма введенных чисел = {list_sum}\nМаксимум введенных чисел = {list_max}\nМинимум введенных чисел = {list_min}\n')
		a = float(input("Введите следующее число цифрой: "))
if a == 7:
	print('«Good bye!»')
'''
print("________________________________________________________________________________________________________________\n"
	  "Благодарю вас за пользование моей программой.\n"
      "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
      "Спасибо за внимание.")



