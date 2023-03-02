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

def math(op, x, y):
    print(op(x, y))

# def calk1(a, b):
#     return a + b
# это тоже самое, что и написанное далее

# calk1 = lambda a, b: a + b
# math(calk1, 5, 45)
# а это тоже, что описано далее

math(lambda a, b: a + b, 5, 45)