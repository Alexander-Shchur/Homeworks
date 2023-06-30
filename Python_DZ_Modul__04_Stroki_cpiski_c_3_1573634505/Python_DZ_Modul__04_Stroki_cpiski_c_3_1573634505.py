print("Добрый день. Это домашняя работа по курсу Python,\nвыполненная студентом группы Python23 академии ТОР, Челябинск\n"
	  "Щур Александром Николаевичем.\nПреподаватель Андрей Комаров\n"
	  "________________________________________________________________________________________________________________")

'''
Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■■ Сформировать третий список, содержащий элементы обоих списков;
■■ Сформировать третий список, содержащий элементы обоих списков без повторений;
■■ Сформировать третий список, содержащий элементы общие для двух списков;
■■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
■■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
'''
import random

joint_list = []
joint_list_no_dubl = []
joint_list_common = []
joint_list_uniq = []
joint_list_min_max = []


a = int(input("Введите первое число цифрой: "))
b = int(input("Введите второе число цифрой: "))
c = int(input("Введите длину списка цифрой: "))


if a < b:
	sample_list_1 = [random.randint(a, b) for i in range(c)]
	sample_list_2 = [random.randint(a, b) for i in range(c)]
else:
	sample_list_1 = [random.randint(b, a) for i in range(c)]
	sample_list_2 = [random.randint(b, a) for i in range(c)]

joint_list = sample_list_1 + sample_list_2

for x in joint_list:
	if x not in joint_list_no_dubl:
		joint_list_no_dubl.append(x)
	elif x in sample_list_1 and x in sample_list_2:
		joint_list_common.append(x)

for i in range(0, len(sample_list_1)):
	if sample_list_1[i] not in sample_list_2:
		joint_list_uniq.append(sample_list_1[i])
	else:
		pass
for k in range(0, len(sample_list_2)):
	if sample_list_2[k] not in sample_list_1:
		joint_list_uniq.append(sample_list_2[k])
	else:
		pass

joint_list_min_max = [max(sample_list_1)] + [min(sample_list_1)] + [max(sample_list_2)] + [min(sample_list_2)]


print(sample_list_1, sample_list_2,joint_list,joint_list_no_dubl,joint_list_common,joint_list_uniq,joint_list_min_max, sep='\n')



print("________________________________________________________________________________________________________________\n"
	  "Благодарю вас за пользование моей программой.\n"
      "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
      "Спасибо за внимание.")
