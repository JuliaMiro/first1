# + 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
# Распечатайте значения 1, 2, 3

# my_list = ['a', 'b', [1, 2, 3], 'd']
# my_list2 = (my_list[2])
# print(my_list2)
# print(my_list2[0])
# print(my_list2[1])
# print(my_list2[2])


# + 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75,
# 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# myList = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

# for item in myList:
#     if isinstance(item, str) and 'a' in item:
#         print(item)

# i = 0
# length = len(myList)
# while i < length:
#     if isinstance(myList[i], str) and 'a' in myList[i]:
#         print(myList[i])
#     i = i + 1

# result = 0
# i = 0
# length = len(myList)
# while i < length:
#     if isinstance(myList[i], int):
#         result = result + myList[i]
#     i = i + 1
# print(result)

# myList2 = filter(lambda val: isinstance(val, int), myList)
# # inspect(myList2)
# myList3 = list(myList2)
# result = sum(myList3)
# print(result)


# + 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# MyList = ['cat', 'dog', 'horse', 'cow']
# Mytuple = tuple(MyList)
# print(Mytuple)
# print(type(Mytuple))

# + 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# family1 = input('enter family 1: ')
# family2 = input('enter family 2: ')
# listFamily1 = family1.split(",")
# listFamily2 = family2.split(",")
# print(type(listFamily1))
# print(type(listFamily2))
# F1 = len(listFamily1)
# F2 = len(listFamily2)
# # print(F1)
# # print(F2)
# if F1 < F2:
#     print('Family 2 is bigger then 1')
# elif F1 > F2:
#     print('Family 1 is bigger then 2')
# else:
#     print('Equal')

# + 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# dct = {'film': 'Best film', 'director': 'famous director', 'year': '2020', 'budget': '232323', 'main actor': 'Superman'}
# print(type(dct))
# for key in dct:
#     print(key)
# for value in dct.values():
#     print(value)
# for key, value in dct.items():
#     print(key, value)

# + 3.6.  Найдите сумму всех значений в словаре
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# from functools import reduce
# result = reduce(lambda x, y: x+y, my_dictionary.values())
# print(result)

# + 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# mylist = [1, 2, 3, 4, 5, 3, 2, 1]
# myset = set(mylist)
# print(mylist)
# newList = list(myset)
# print(newList)

# + 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
# - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# a = set1.intersection(set2)
# print(a)
# b = set1.symmetric_difference(set2)
# print(b)
# print(set1.issubset(set2))
# print(set2.issubset(set1))
