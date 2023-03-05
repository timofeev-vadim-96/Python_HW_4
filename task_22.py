# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите размер первого множества: '))
m = int(input('Введите размер второго множества: '))

list_1, list_2= [random.randint(1,n+1) for x in range(n)], [random.randint(1,n+1) for x in range(n)] # задаем списки
multitude_1, multitude_2 = set(list_1), set(list_2) # конвертируем в множества, убирая не уникальные э-ты
print(f'Первое множество: {multitude_1}\nВторое множество: {multitude_2}')
list_res = list(multitude_1.intersection(multitude_2)) # создаем список из пересечения двух множеств

def bubble_sorting(input_list): # ПУЗЫРЬКОВАЯ СОРТИРОВКА
    for i in range(0, len(input_list)):
        for j in range (1, len(input_list)-i):
            if input_list[j] < input_list[j-1]:
                temp = input_list[j]
                input_list[j] = input_list[j-1]
                input_list[j-1] = temp
    return input_list

bubble_sorting(list_res) # сортируем результирующий список
print(f'Отсортированное пересечение двух множеств : {list_res}')

