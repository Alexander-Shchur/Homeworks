'''
Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя
программа выводит на экран сумму трёх чисел или произведение трёх чисел.
'''

a = input("Добро пожаловать. Вам необходимо ввести три числа. \n Введите первое число:")
b = input("Введите второе число:")
c = input("Введите третье число:")

if a == int or float and b == int or float and c == int or float:

    choice = input("Выберите желаемое математическое действие: \n "
               "1 - Сложение трех введенных чисел \n "
               "2 - Умножение трех веденных чисел\n")


    if choice == "1":
        print(f"Сумма введенных чисел равна: {a + b + c} \n"
      "_________________________________________________________________________________")
    elif choice == "2":
        print(f"Произведение введенных чисел равно: {a * b * c} \n"
      "_________________________________________________________________________________")

    else:
        print(f"Неверный ввод. Запустие программу еще раз.\n"
    "_________________________________________________________________________________")

else:
    print(f"Неверный ввод. Запустие программу еще раз.\n"
    "_________________________________________________________________________________")

print("Благодарю вас за пользование моей программой.\n"
  "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
  "Спасибо за внимание.")