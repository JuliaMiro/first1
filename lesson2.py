# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False,
# в противном случае True.

# health = int(input('enter health:'))
# if health <= 0:
#     print(False)
# else:
#     print(True)

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное
# число четным. Если да, выведите на экран текст “Четное”,
# а иначе - “Нечетное”

# num = input('введи число:')
# if int(num) == 0:
#     print('это 0')
# elif int(num) % 2:
#     print('нечетное')
# else:
#     print('четное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4
# (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400,
# он также считается високосным (1200, 2000)

# year = input('please, enter year:')
# if int(year) == 0:
#     print('year 0')
# elif int(year) % 100 ==0 and int(year) % 400 !=0:
#     print("not a leap year")
# elif int(year) % 4 == 0:
#     print('a leap year')
# else:
#     print("not a leap year")

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное
# количество раз, построчно. Текст и количество повторений нужно
# ввести с помощью input()

# text = input('please, enter a word:')
# quantity = input('number of lines:')
# i = 0
# if int(quantity) <= 0:
#     print("number of lines have to be > 0")
# else:
#     while i != int(quantity):
#         print(text)
#         i = i + 1

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два
# числа и оператор (в формате str), производит заданное
# арифметическое действие и печатает результат в формате:
# {num1} {operator) {num2) = {result}

# num1 = int(input('enter number 1: '))
# num2 = int(input('enter number 2: '))
# operator = input('enter operator: ')
# if operator == "*":
#     result = num1 * num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif operator == "+":
#     result = num1 + num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif operator == "-":
#     result = num1 - num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f'{num1} {operator} {num2} = {result}')
#     else:
#         print('на 0 не делим тут')
# else:
#     print('operator not available')


