# Задача 0
# Написать прогорамму сложения двух чисел
# # простой способ
# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {x + y}')

# # через метод
# def sum(a, b):
#     return a + b

# x = int(input('x = '))
# y = int(input('y = '))
# print(f'{x} + {y} = {sum(x, y)}')

# через лямбду
sum = lambda a, b: a + b

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x, y)}')