# def number_to_string(num):
#     a = int (input("DD"))
#     b = str(a)
#     return b
#
# def repeat_str(repeat, string):
#     s = input("enter the word")
#     n = int(input("enter the number"))
#     i = 0
#     if int(n) <= 0:
#         print("the number must be > 0")
#     else:
#         while i != n:
#             print(s)
#             i = i + 1
#     return s
import collections


# def bool_to_word(boolean):
#     if boolean == "true":
#         return "YES"
#     else:
#         return "No"
#
# a = bool_to_word("false")
# print(a)
#
# def solution(string):
#     return reversed(string)

# def solution(string):
#  return (string[::-1])
# a = solution("world")
# print(a)

#
# def build_string(*args):
#  return "I like {1}!".format(",".join(args))
#
# def build_string(*args):
#  return "I like {1}!".format(",".join(args))


# def sum_str(a, b):
#  if a != "" and b != "":
#   return str(int(a) + int(b))
#  elif a == "" and b !='':
#   return str(0 + int(b))
#  elif b == "" and a !='':
#   return str(int(a) + 0)
#  else:
#   return 0
#
# d = sum_str('', '')
# print(d)

# def is_uppercase(inp):
#  if str.istitle(inp):
#   return 'True'
#  else:
#   return "False"
#
# a = is_uppercase("g")
# print(a)

# def is_uppercase(inp):
#   if str.isupper(inp):
#    return True
#   else:
#    return False

# import re
# def is_uppercase(inp):
#     if inp.upper() == inp:
#         return True
#     elif re.match('[a-z]',inp) != None:
#         return False
#     else:
#         return False
#
# # ss = "helloIAMDONALD"
# ss = "$%&S"
# print(str.isupper(ss))
# # print(str.istitle(ss))
# # print(is_uppercase(ss))

# def is_uppercase(inp):
#     if inp.upper == inp:
#         return True
#     else:
#         return False
#
# d = "dd"
# s = d.upper()
# print(s)

# def greet(name):
#     return f"Hello, {name} how are you doing today?"
#
# s = greet('ffff')
# print(s)

# def abbrev_name(name):
#     name1 = name.upper()
#     return ('.'.join([i[0] for i in name1.split()]))
#
# a = abbrev_name("hjr Bty")
# print (a)



#
# d = "fdfdfdf"
# s = d.upper()
# print(s)
#
# def high_and_low(numbers):
#     nums = [int(i) for i in numbers.split()]
#     return " ".join([str(max(nums)), str(min(nums))])

#
# def high_and_low(numbers):
#     nums = [int(i) for i in numbers.split()]
#     print(nums)
#     return " ".join([str(max(nums)), str(min(nums))])
# d = high_and_low("4 5 -9 13 245")
# print(d)

# def high_and_low(numbers):
#     numbers2 = list(map(int, numbers.split()))
#     return f'{max(numbers2)} {min(numbers2)}'

# d = high_and_low("34 -4 5 56 -29 13 245")
# print(d)

# def xo(s):
#     w = list(s)
#     if sum('x') == sum('o') in w:
#         return True
#     else:
#         return False

# a = xo('xoxo')
# print(a)
# from collections import Counter
# d = 'ooXx'
# w = d.upper()
# print(w)
# counter = Counter(w)
# print(counter['X'])
# print(counter['O'])
# if counter['X'] == counter['O']:
#     print (True)
# else:
#     print(False)
def no_space(x):
    return x.replace(" ", "")

d = "fgfg gfg gfg"
s = d.replace(" ","")
print(s)

# def is_f(n):
#     if type(n) == int and int(n) % 2 ==0 or int(n)/float(n)== 1.0 and int(n) % 2 == 0:
#
#         print(True)
#     else:
#         print(False)
#
#
# s = is_f(6.0)

# def remuve_d(s):
#     d = s[1:]
#     w = d[:-1]
#     return w
#
# e = remuve_d("4, 5, 6, 7")
# print(e)

# def string_to_array(s):
#     return  s.split()
#
#
# a = string_to_array("Guhj lkhsflk dfsdf")
# print(a)

# def rev(s):
#     return list(s, )
#
# a = rev("s df fgg ghjj kkjjj")
# print(a)

# def two_decimal_places(number):
#     return float(str(round(number, 3)) [:-1])
#
# d = two_decimal_places(-892616.238787)
# print(d)

# def calculate(num1, operation, num2):
#     if operation == "+":
#         return num1 + num2
#     elif operation == "-":
#         return num1 - num2
#     elif operation == "*":
#         return num1 * num2
#     else:
#         return num1/num2
#
# d = calculate(2, "+", 4)
# print(d)

# def basic_op(operator, value1, value2):
#     if operator == "+":
#         return value1 + value2
#     elif operator == "-":
#         return value1 - value2
#     elif operator == "*":
#         return value1 * value2
#     elif operator == "/":
#         if value2 !=0:
#             return value1 / value2
#     else:
#         return None
#
# d = basic_op("+", 4, 7)
# print(d)

# def switch_it_up(number):
#     if number ==1:
#         return "One"
#     elif number ==2:
#         return "Two"
#     elif number ==3:
#         return "Three"
#     elif number ==4:
#         return "Four"
#     elif number ==5:
#         return "Five"
#     elif number ==6:
#         return "Six"
#     elif number ==7:
#         return "Seven"
#     elif number ==8:
#         return "Eight"
#     elif number ==9:
#         return "Nine"
#     else:
#         return "Zero"

# def area_or_perimeter(l, w):
#     if l==w:
#         return l * w
#     else:
#         return 2*l + 2*w

# def bmi(weight, height):
#     d = round((weight/(height*height)), 1)
#     if d <= 18.5:
#         return "Underweight"
#     elif d <= 25.0:
#         return "Normal"
#     elif d <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"
#
# r = bmi(134, 1)

# def twice_as_old(dad_years_old, son_years_old):
#     a = dad_years_old
#     b = son_years_old
#     f = ((a - b)*2 - a)
#     if f >=0:
#         return f
#     else:
#         return 0-f

# def get_grade(s1, s2, s3):
#     d = (s1 + s3 + s2)/3
#     if d <= 100 and d >= 90:
#         return "A"
#     elif d < 90 and d >= 80:
#         return "B"
#     elif d < 80 and d >=7 0:
#         return "C"
#     elif d < 70 and d >= 60:
#         return "D"
#     elif d < 60 and d >=0:
#         return "F"
#     else:
#         return None

# def chromosome_check(sperm):
#     if "Y" in sperm:
#         return "Congratulations! You're going to have a son."
#     else:
#         return "Congratulations! You're going to have a daughter."
#
# d = chromosome_check("XY")
# print(d)

# def fuel_price(litres, price_per_litre):
#     if litres < 2:
#         return round(price_per_litre, 2)
#     elif litres >= 2 and litres < 4:
#         return round(((price_per_litre - 0.05)*litres), 2)
#     elif litres >= 4 and litres < 6:
#         return round(((price_per_litre - 0.10)*litres), 2)
#     elif litres >= 6 and litres < 8:
#         return round(((price_per_litre - 0.15)*litres), 2)
#     elif litres >= 8 and litres < 10:
#         return round(((price_per_litre - 0.20)*litres), 2)
#     else:
#         return round(((price_per_litre - 0.25)*litres), 2)
#
# d = fuel_price(5, 2.47)
# print(d)

# def calculate_age(year_of_birth, current_year):
#     if year_of_birth == current_year:
#         return "You were born this very year!"
#     elif year_of_birth > current_year:
#         if year_of_birth - current_year != 1:
#             return f"You will be born in {year_of_birth - current_year} years."
#         else:
#             return f"You will be born in {year_of_birth - current_year} year."
#     else:
#         if current_year - year_of_birth != 1:
#             return f"You are {current_year - year_of_birth} years old."
#         else:
#             return f"You are {current_year - year_of_birth} year old."
#
#
#
# f = calculate_age(2010, 2012)
# print(f)

# def hoop_count(n):
#     if n >= 10:
#         return "Great, now move on to tricks"
#     else:
#         return "Keep at it until you get it"

# def plural(n):
#     if n != 1:
#         return True
#     else:
#         return False

# def enough(cap, on, wait):
#         d = wait - (cap - on)
#         if d > 0:
#             return d
#         else:
#             return 0
#
# s = enough(20, 5, 5)
# print (s)

# def problem(a):
#     if a == str(a):
#         return "Error"
#     else:
#         return a*50+6
#
# s = problem("f")
# print(s)

# def break_chocolate(n, m):
#     if n == 1 and m != 1:
#         return m - 1
#     elif m == 1 and n != 1:
#         return n - 1
#     elif m == 0 or n == 0:
#         return 0
#     elif n != 1 and m != 1:
#         return m * n - 1
#     else:
#         return 0
#
# def breakChocolate(n, m):
#     return max(n*m-1,0)

# def correct(s):
#     return s.replace('1', 'I').replace('0', 'O').replace('5', 'S')
#
#
#
# d = correct("1234567890")
# print(d)
#
#
# def rental_car_cost(d):
#     if d < 3:
#         return 40 * d
#     elif 3 <= d < 7:
#         return 40 * d - 20
#     else:
#         return 40 * d - 50
#
# a = rental_car_cost(7)
# print(a)
#
# def arithmetic(a, b, operator):
#     if operator == "add":
#         return a + b
#     elif operator == "subtract":
#         return a - b
#     elif operator == "divide":
#         return a / b
#     else:
#         return a * b

# from operator import add, mul, sub, truediv
# def arithmetic(a, b, operator):
#     ops = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}
#     return ops[operator](a, b)
# s = arithmetic(2, 3, "add")
# print(s)
#
# def check(seq, elem):
#     if elem in seq:
#         return True
#     else:
#         return False

# def how_much_i_love_you(nb_petals):
#     if nb_petals % 6 == 1:
#         return "I love you"
#     if nb_petals % 6 == 2:
#         return "a little"
#     if nb_petals % 6 == 3:
#         return "a lot"
#     if nb_petals % 6 == 4:
#         return "passionately"
#     if nb_petals % 6 == 5:
#         return "madly"
#     if nb_petals % 6 == 0:
#         return "not at all"

# def array_plus_array(arr1,arr2):
#     return sum(arr1) + sum(arr2)
#
# s = array_plus_array([1,2], [2,3])
# print(s)
#
# def number(lines):
#     return dict(lines)
#
# s = number(["w", 'e', 'r'])
# print(s)

# def count_sheeps(sheep):
#     sheep_1 = filter(lambda x: x == True, sheep)
#     return len(list(sheep_1))
#
# d = count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True])
# print(d)

# def digitize(n):
#     n1 = str(n)
#     n2 = list(n1)
#     n3 = list(reversed(n2))
#     result = [int(i) for i in n3]
#     return result
#
# s = digitize(35231)
# print(s)

def array(string):
    string1 = string.replace(',', " ") #удаляем запятые
    print(string1)
    d = string1.split()    # получаем лист с элементами по пробелу
    print(d)
    # print(type(d))
    # print(len(d))
    if len(d) > 2:
        r = d[1 : -1] #оставляем все кроме 1 и посл элемента
        print(r)
        new_string = ''
        return " ".join(r)
    else:
        return None


f = array("0,32,4,6,ce3,5f6,1e4,fc")
print(f)