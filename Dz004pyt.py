# z22.Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.



#etalon
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#   print(i, end = ' ')

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)

#z24.
#etalon
# n = int(input('Vvedite kolvo kustov  '))
# arr = list()
# for i in range(n):
#     x = int(input('Vvedite nomer kusta '))
#     arr.append(x)

# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr [i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr [0])
# print(max(arr_count))



# from random import randint
# list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
# print(list_1)
# a = int(input('Введите № куста: '))
# res = 0
# if a == 1:
#     res = list_1[0] + list_1[1] + list_1[-1]
# elif a == len(list_1):
#     res = list_1[-2] + list_1[-1] + list_1[0]
# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
# print(res, 'ягод')

