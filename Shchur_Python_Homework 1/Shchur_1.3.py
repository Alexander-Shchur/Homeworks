'''
Пользователь вводит с клавиатуры количество метров. В зависимости от выбора
 пользователя программа переводит метры в мили, дюймы или ярды.
'''


a = int(input("Добро пожаловать. Вам необходимо ввести значение в метрах. \n Введите значение:"))

choice = input("Выберите единицу, в которую хотите перевести введенное значение: \n "
                   "1 - Перевести метры в мили \n "
                   "2 - Перевести метры в дюймы\n "
                   "3 - Перевести метры в ярды\n")

if choice == "1":
    print(f"При переводе введенного числа метров в мили получим: {a * 0.000621371} мили.\n"
          "_________________________________________________________________________________")

if choice == "2":
    print(f"При переводе введенного числа метров в дюймы получим: {a * 39.3701} дюйма.\n"
          "_________________________________________________________________________________")

if choice == "3":
    print(f"При переводе введенного числа метров в ярды получим: {a * 1.09361} ярда.\n"
          "_________________________________________________________________________________")

else:
    print(f"Неверный ввод. Запустие программу еще раз.\n"
    "_________________________________________________________________________________")

print("Благодарю вас за пользование моей программой.\n"
      "Направляйте свои замечания на электронную почту alexandershchoor@gmail.com.\n"
      "Спасибо за внимание.")