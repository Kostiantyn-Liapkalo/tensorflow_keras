# Визначимо функцію f(x)
def f(x):
    if x == 0:
        return "Функція не визначена при x = 0"
    else:
        absolute_x = abs(x)
        result = (1 + absolute_x) / x
        return result

# Приклад використання функції
x = 3  # Замість 3 можна вказати будь-яке інше значення x, крім 0
result = f(x)
print(f'f({x}) = {result}')

x = -5
absolute_x = abs(x)
print(absolute_x)  # Результат буде 5, оскільки abs(-5) = 5

# Визначимо функцію f(x)
def f(x):
    if x >= 0:
        return x
    else:
        return 0

# Приклад використання функції
x = -3  # Замість 3 можна вказати будь-яке інше значення x
result = f(x)
print(f'f({x}) = {result}')

import math


# Визначимо функцію phi
def phi(vi, ci, sigma):
    # Обчислюємо квадрат відстані між vi і ci
    distance_squared = sum((vi[j] - ci[j]) ** 2 for j in range(len(vi)))

    # Обчислюємо phi(vi) за формулою
    result = math.exp(-distance_squared / (2 * sigma ** 2))

    return result


# Приклад використання функції
vi = [1.0, 2.0, 3.0]  # Вектор vi
ci = [0.0, 0.0, 0.0]  # Центр ci
sigma = 1.0  # Значення sigma

result = phi(vi, ci, sigma)
print(f'phi(vi) = {result}')

import math


# Визначимо функцію phi
def phi(vi, x, beta0, beta1):
    # Обчислюємо суму vi[j] * x[j]
    sum_vi_x = sum(vi[j] * x[j] for j in range(len(vi)))

    # Обчислюємо аргумент гіперболічного тангенсу
    argument = beta1 + beta0 * sum_vi_x

    # Обчислюємо phi(vi) за допомогою гіперболічного тангенсу
    result = math.tanh(argument)

    return result


# Приклад використання функції
vi = [1.0, 2.0, 3.0]  # Вектор vi
x = [0.5, -1.0, 2.0]  # Вектор параметрів x
beta0 = 0.2  # Значення beta0
beta1 = 0.1  # Значення beta1

result = phi(vi, x, beta0, beta1)
print(f'phi(vi) = {result}')
