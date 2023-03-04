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

# Теперь решим эту задачу при помощи lambda-функции
def select(f, col):
    return[f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)
