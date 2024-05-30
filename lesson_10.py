# Задача1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# n = int(input("Введите расстояние в день: "))
# m = int(input("Введите необходимое расстояние: "))
# res = int((m-1)/n) + 1
# print(res)

# Задача №3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# a = int(input("Введите количество учащихся в 1 классе: "))
# b = int(input("Введите количество учащихся в 2 классе: "))
# c = int(input("Введите количество учащихся в 3 классе: "))
# m = a//2 + a%2 + b//2 + b%2 + c//2 + c%2
# print(f'Минимальное колмчество парт {m}')

# Задача №9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# n = int(input("Введите число: "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print(f'Факториал числа {n} равен: {factorial}')

# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# A = int(input("Введите число: "))
# temp = 0
# n1 = 1
# n2 = 1
# counter = 2 #первые три числа известны
# while temp < A:
#     temp = n1 + n2 #сложили два последних
#     n1 = n2 #перенесли предпоследнее 
#     n2 = temp #вместо предпоследнего записали последнее
#     counter += 1
#     if temp > A:
#         counter = 0    
# if counter != 0:
#     print(counter)
# else:
#     print(-1)
    
# Задача №13. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# day = int(input("Введите количество дней: "))
# max_counter = 0
# counter = 0

# for _ in range(day):
#     temp = int((input("Температура: ")))
#     if temp > 0:
#         counter +=1
#     else:
#         counter = 0
#     if counter > max_counter:
#         max_counter = counter
# print(max_counter)

# Задача №15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# N = int(input("Количество арбузов: "))
# for i in range(N):
#     weight = int(input("Вес арбуза: "))
#     if i == 0:
#         min_weight = weight
#         max_weight = weight
#         continue
#     if weight < min_weight:
#         min_weight = weight
#     elif weight > max_weight:
#         max_weight = weight
# print(min_weight, "для тещи")
# print(max_weight, "для себя")

#Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# list_1 = [1,1,2,2,3,3,4,4]
# result_list = list()
# for i in list_1:    #для каждого элемента в list_1
#     if i not in result_list:
#         result_list.append(i)
# print(result_list)
# print(len(result_list))

# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# list_1 = [1,2,3,4,5,6,7]
# k = 3
# # выполняем циклический сдвиг
# shifted_list = list_1[k:] + list_1[:k]
# print("После сдвига:", shifted_list)

# Задача №21. Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}] 
# dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# dict_2 = set()
# # проходим по каждому словарю в списке
# for dictionary in dict_1:
#     # проходим по каждому значению в словаре
#     for value in dictionary.values():
#         # добавляем значение в множество
#         dict_2.add(value)
# print(dict_2)

# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)
# arr = [0, -1, 5, 2, -5, -6, 12, 13, 15, 18]
# n = 0
# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         n +=1
# print(n)

# Как выбрать ключи и значения из словаря
# contacts = {"мама": 123456, "папа": 789123, "брат": 456789}
# for i in contacts: #по умолчанию проходим по ключам
#     print(i)

# for key in contacts.keys(): #проходим именно по ключам
#     print(key)

# for number in contacts.values(): #проходим только по значениям
#     print(number)

# for cont,number in contacts.items(): #проходим и по ключам и по значениям
#     print(number,cont)                 # при выводе можно поменять местами ключ и значение


# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# string = input("Введите строку: ").split() #вводим строку и сразу преобразуем ее в список
# result = dict()                             #создаем словарь
# for i in string:                            #перебираем список
#     if i in result.keys():                  #если в списке уже есть символ (ключ)
#         print(f'{i}_{result[i]}', end=" ")  #печатаем ключ с значением и увеличиваем его на 1
#         result[i] +=1
#     else:
#         print(i, end=" ")
#         result[i] = 1
# print(result)


# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# string = '''She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore,I'm sure that the shells are sea shore shells'''
# string_new = string.lower().split()     #убираем строчные буквы и преобразуем ее в список
# print(string_new)
# string_new = set(string_new)            #преобразуем список в множество (только уникальные элементы)
# print(len(string_new))                  #печатаем количество элементов в множестве


# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”
# Maximum = 0
# number = None
# while number != 0:
#     number = int(input("Введите неотриц. число: "))
#     if number > Maximum:
#         Maximum = number
# print(Maximum)


# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# def revers(grades):
#     min_grade = min(grades)
#     max_grade = max(grades)
#     list1 = []
#     for grade in grades:
#         if grade == max_grade:
#             list1.append(min_grade)
#         else:
#             list1.append(grade)
#     return list1

# print(revers([1, 5, 4, 5, 3]))


# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# def simple(N):
#     if N % 2 == 0:
#         return 'no'
#     for i in range(3, N//2, 2):
#         if N % i == 0:
#             return 'no'
#     return 'yes'

# print(simple(12))


# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# import random
# def list_creator(num):
#     list = []
#     for i in range(num):
#         list.append(random.randint(1, 10))
#     return list

# def list_compear(list1, list2):
#     list = []
#     for i in list1:
#         if i not in list2:
#             list.append(i)
#     return list

# n = int(input('Введите количество элементов массива n: '))
# m = int(input('Введите количество элементов массива m: '))
# list_1 = list_creator(n)
# list_2 = list_creator(m)
# print(list_1)
# print(list_2)
# list_3 = list_compear(list_1, list_2)
# print(list_3)

# # Cоздание списка:
# nums = []
# for i in range(5):
#     n = int(input('Введите число: '))
#     nums.append(n)
# # Сокращаем запись:
# nums = []
# for i in range(5):
#     nums.append(int(input('Введите число: ')))
# # Еще сокращаем запись:
# nums = [int(input('Введите число: ')) for i in range(5)]
# # Строим функцию:
# def create_arr(lenght):
#     nums = [int(input('Введите число: ')) for i in range(lenght)]

# create_arr(int(input('Введите длинну массива: ')))

# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# def create_arr(lenght):
#     nums = [int(input('Введите число: ')) for i in range(lenght)]
#     return(nums)

# arr = create_arr(int(input('Введите длинну массива: ')))
# print(arr)
# n = 0
# for i in range(1, len(arr)-1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         n +=1
# print(n)

# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# num = 0
# for i in range(len(arr)-1):
#     for j in range(i+1, len(arr)):
#         if arr[i] == arr[j]:
#             num +=1
# print(num)

# Задача. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)
#улучшаем, используя lambda функцию
# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x%2==0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

#Использование функции map
# list_1 = [x for x in range(1, 20)] #генератор списков
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1)) #принимает объект и функцию, которая применяется к каждому элементу объекта
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# data = '15 156 96 3 5 8 52 5'
# data = list(map(int, data.split()))
# print(data)

#Использование функции filter
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x%10==5, data)) #принимает объект и отделяет элементы, которые соответствуют условию
# print(res)

# Задача №49. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
#orbits = [(1, 3), (2.5, 10), (7, 12), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#     s_orbits=list(map(lambda i: i[0]*i[1] if i[0]!=i[1] else 0, orbits)) #создаем новый список из площадей орбит при помощи функции map
#                                                                         #замещает цикл for, добавлено условие неравенства полуосей
#     max_sum = max(s_orbits)                                             #функция max возвращает максимальный элемент списка s_orbits                       
#     max_index = s_orbits.index(max_sum)     #функция index возвращает индекс заданного значения
#     return orbits[max_index]
# print(find_farthest_orbit(orbits))
#Другое решение:
# def find_farthest_orbit(orb):
#     return max(orb, key=lambda i: i[0]*i[1] if i[0]!=i[1] else 0)   #сразу возвращает максимальное значение рассчитанное выражением

# print(*find_farthest_orbit(orbits))     #звездочка * убирает скобки при печати

# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
#values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) in [0,1] #возвращает все ли элементы списка удовлетворяют условию или все не удовлетворяют

# print(same_by(lambda x: x % 2, values))

# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!
# def print_operation_table(operation, num_rows=None, num_columns=None):
#     if num_rows == None:
#         num_rows = 9
#     if num_columns == None:
#         num_columns = 9
#     if num_rows <= 2 or num_columns <= 2:
#         return print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     for i in range(1, num_rows+1):
#         num = []
#         for j in range(1, num_columns+1):
#             num.append(operation(i,j))
#         print (*num)
#     return

# print_operation_table(lambda x, y: x * y)

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, 
# если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.
# stroka = 'по-русски говорят'

# def poem(str):
#     string = str.lower().split()
#     print(string)
#     if len(string) < 2:
#         return 'Количество фраз должно быть больше одной!'
#     print(string[0])
#     num = string[0].count('а') + string[0].count('о') + string[0].count('и') + string[0].count('е') + string[0].count('у') + string[0].count('ы') +string[0].count('ю') + string[0].count('э') + string[0].count('я') +string[0].count('ё')
#     print(num)
#     for i in range(1, len(string)):
#         print(string[i])
#         print(string[i].count('а') + string[i].count('о') + string[i].count('и') + string[i].count('е') + string[i].count('у') + string[i].count('ы') +string[i].count('ю') + string[i].count('э') + string[i].count('я') +string[i].count('ё'))
#         if string[i].count('а') + string[i].count('о') + string[i].count('и') + string[i].count('е') + string[i].count('у') + string[i].count('ы') +string[i].count('ю') + string[i].count('э') + string[i].count('я') +string[i].count('ё') != num:
#             return 'Пам парам'
#     return 'Парам пам-пам'

# print(poem(stroka))

#вариант 2 (не работает)
# def count_vowels(string):
#     vowels = "ёйуеыаоэяию"
#     phrases = string.split()
#     if len(phrases) < 2:
#         return 'Количество фраз должно быть больше одной!'
#     counters = set()
#     for phrase in phrases:
#         counters.add(len((letter for letter in phrase if letter in vowels)))
#     if len(counters) == 1:
#         return 'Парам пам-пам'
#     else:
#         return 'Пам парам'

# print(count_vowels(stroka))

# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# contact_data = {
#     'ferst_name': None,
#     'second_name': None,
#     'phone_number': None
# }


# def ask_data():
#     f_name = input("Введите имя: ")
#     m_name = input("Введите отчество: ")
#     s_name = input("Введите фамилию: ")
#     phone = input("Введите номер телефона: ")
#     contact = {'ferst_name': f_name,
#         'middle_name': m_name,
#         'second_name': s_name,
#         'phone_number': phone}
#     return contact

# def add_new_contact():
#     contact = ask_data()
#     with open('phonebook.txt', 'a', encoding='utf-8') as file:
#         for value in contact.values():
#             file.write(f"{value}; ")
#         file.write('\n')
#     return True

# def open_phonebook():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         for line in file:
#             print("\t\t".join(line.split(";")))

# def find_contact():
#     title = ["Фамилия", "Имя", "Отчество", "Телефон"]
#     print(f'Поиск по:\n1 Имени\n2 Фамилии\n3 Отчеству\n4 Телефону\n0 выход')
#     s_name = input("Введите фамилию: ")
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         print("\t\t".join(title))
#         for line in file:
#             line = line.split()
#             if s_name in line[0]:
#                 print("\t\t".join(line))

# def main():
#     isStop = 10
#     while isStop != 0:
#         print(f'Выберете что хотите сделать:\n1 посмотреть\n2 добавить\n3 сохранить\n4 открыть\n5 копировать\n0 выход')
#         isStop = int(input(">"))
#         if isStop == 1:
#             find_contact()
#         elif isStop == 2:
#             add_new_contact()
#         elif isStop == 4:
#             open_phonebook()
#         input('Нажмите Enter чтобы продолжить')


# main()

# import pandas as pd

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для one-hot encoding
one_hot_df = pd.DataFrame(columns=['robot', 'human'])

# Проходим по строкам и заполняем one-hot DataFrame
for index, row in data.iterrows():
    if row['whoAmI'] == 'robot':
        one_hot_df.loc[index] = [1, 0]
    else:
        one_hot_df.loc[index] = [0, 1]

one_hot_df.head()
print(one_hot_df.head())


# """username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Мы вас ждали, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)"""
