# ++ 4.1. Напишите функцию square, принимающую 1 аргумент —
# сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
# import cmath
# def square(a):
#      return a * 4, a**2, cmath.sqrt(2*a**2), (2*a**2)**0.5
# w = square(5)
# print(w)
# print(type(w))

# ++ 4.2. Напишите фукнцию, которая принимает произвольное количество
# именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def about(**kwargs):
#     for key, value in kwargs.items():
#         print(key,':', value)
# a = about(a=[1, 7], c=26, d="jkhkjh")


# ++ 4.3. Используя лямбда-выражение, из списка
# my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# my_list1 = filter(lambda x: x>0, my_list)
# print(list(my_list1))


# ++ 4.4. Используя лямбда выражение, получите результат перемножения
# значений в предыдущем списке
# import functools
# my_list = [20, -3, 15, 2, -1, -21]
# # my_list = [1, 2, 3, 4, 5]
# my_list1 = functools.reduce(lambda x, y: x * y, my_list)
# print(my_list1)


# ++ 4.5. Напишите декоратор, который высчитывает время работы
# функции, которую он принимает в качестве параметра
import time


def my_decoratortime(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        print(time.perf_counter() - start_time)
        return result
    return wrapper()


def new(*args):
    result = filter(lambda x: x > 5, list(args))
    return result
# my_list = new(6, 7, 9, 3, 5, 7)
# print(list(my_list))

@my_decoratortime
def test_f():
    return new(6, 7, 9, 3, 2)


# time999 = my_decoratortime(test_f)
# print(type(time999))

# ++ 4.6. Создайте файл my_calc.py и пропишите в нем минимум
# 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.

# from my_calc import plus
# result1 = plus([4, 10, 5])
# print(result1)
#
# from my_calc import minus
# result2 = minus(12, 34)
# print(result2)
#
# from my_calc import mult
# result3 = mult(3, 4)
# print(result3)
#
# import my_calc
# result4 = my_calc.div(9, 8)
# print(result4)


# git check
# a = f + c

def mult(a, b):
    return a * b