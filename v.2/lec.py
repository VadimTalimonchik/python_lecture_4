# def f(x):
#     return x ** 2
# print(f(2))
# print(type(f))

# a = f
# print(type(a))
# print(a(5))

# ------------------
# def calk1(a):
#     return a + a

# def calk2(a):
#     return a * a

# def math(op, x):
#     print(op(x))

# math(calk2, 5)

# ------------------
# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 45)

# --------------------
# lambda-функции

# def math(op, x, y):
#     print(op(x, y))

# # def calk1(a, b):
# #     return a + b
# # это тоже самое, что и написанное далее

# # calk1 = lambda a, b: a + b
# # math(calk1, 5, 45)
# # а это тоже, что описано далее

# math(lambda a, b: a + b, 5, 45)

# -----------------
# Задача 1
# В списке хранятся числа. Нужно выбрать только чётные числа и
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]  # имеем список
# res = list()                        # создаём новый пустой список в который будет заноситься результат

# for i in data:                      # пройдём по всем элементам списка data
#     if i % 2 == 0:                  # проверяем если переменная i делится 2 без остатка, т.е. элемент чётный
#         res.append((i, i ** 2))     # то в список res будем добавлять новые значения i и через запятую
#                                     # указываем i**2 и это передаём в виде кортежа, т.к. переменные
#                                     # заключены в скобки
# print(res)                          # выведем результат res

# # Теперь решим эту задачу при помощи lambda-функции
# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# ФУНКЦИЯ map

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этон набор чисел будет считан в качестве строки. Как превратить list строк в
# list чисел?
# data = '15 156 96 3 5 8 52 5'
# print(data)

# data = data.split()
# print(data)

# применим функцию map
# data = '15 156 96 3 5 8 52 5'

# data = list(map(int, data.split()))
# print(data)

# отсылка к прошлой задаче
# def select(f, col):
#     return[f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)